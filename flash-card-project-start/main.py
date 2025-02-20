from tkinter import Tk, Canvas, PhotoImage, Button
import pandas
import random
import time

# TODO-2 FIND A WAY TO DISPLAY THE DATA ON THE CARD UI USING PANDANS
try:
    data_frame = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data_frame=pandas.read_csv("./data/french_words.csv")
# else:
#     data_frame=pandas.read_csv("./data/words_to_learn.csv")


new_data = data_frame.to_dict(orient="records")
random_row={}


# french_word=data_frame["French"]
# random_french_word=random.choice(french_word)

# random_data=data_frame.sample()
# random_data_index=random_data.index[0]
# french_word=data_frame.loc[random_data_index,"French"]
# translation_word=data_frame.loc[random_data_index,"English"]
# print(f"{french_word}--{translation_word}")


# print(f"{french_word}----{translation_word}")


def generate_random_word():
    generate_random_word_cancel()
    new_data.remove(random_row)
    data=pandas.DataFrame(new_data)
    data.to_csv("./data/words_to_learn.csv")


def generate_random_word_cancel():
    global random_row
    random_row = random.choice(new_data)
    french_word = random_row["French"]
    canvas.itemconfig(word_text, text=french_word, fill="black")
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(card_image, image=card_front)#
    window.after(3000,func=flip_card)


def flip_card():
    translation_word = random_row["English"]
    canvas.itemconfig(word_text, text=translation_word, fill="white")
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(card_image, image=new_image)


BACKGROUND_COLOR = "#B1DDC6"
# TODO-1 CREATE THE UI FOR THE GAME BY USING THE TKINTER MODULE
window = Tk()
window.title("Flash Card Generator")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.after(3000, func=flip_card)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
new_image = PhotoImage(file="./images/card_back.png")
card_image = canvas.create_image(400, 526 / 2, image=card_front)
title_text = canvas.create_text(400, 150, text="Title", font=("Arial", 30, "italic"))
word_text = canvas.create_text(400, 263, text="french", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

cancel_image = PhotoImage(file="./images/wrong.png")
cancel_button = Button(image=cancel_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=generate_random_word_cancel)
cancel_button.grid(column=0, row=1)

activate_image = PhotoImage(file="./images/right.png")
activate_button = Button(image=activate_image, highlightthickness=0, command=generate_random_word)
activate_button.grid(column=1, row=1)

generate_random_word()

window.mainloop()
