import random
import pandas
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
word_to_learn = {}
random_word = {}

try:
    words = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_words = pandas.read_csv("data/french_words.csv")
    word_to_learn = original_words.to_dict(orient="records")
else:
    word_to_learn = words.to_dict(orient="records")

def next_word():
    global random_word, flip
    window.after_cancel(change_language)
    random_word = random.choice(word_to_learn)
    canvas.itemconfig(card, image=front)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=random_word["French"], fill="black")
    flip = window.after(3000, func=change_language)

def known():
    word_to_learn.remove(random_word)
    words_to_learn = pandas.DataFrame(word_to_learn)
    words_to_learn.to_csv("data/words_to_learn.csv", index=False)
    next_word()

def change_language():
    canvas.itemconfig(card, image=back)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=random_word["English"], fill="white")

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip = window.after(3000, func=change_language)

front = PhotoImage(file="images/card_front.png")
back = PhotoImage(file="images/card_back.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card = canvas.create_image(400, 263, image=front)
canvas.grid(row=0, column=0, columnspan=2)

language = canvas.create_text(400, 150, text='', font=('arial', 40, 'italic'))
word = canvas.create_text(400, 283, text='', font=('arial', 60, 'bold'))

correct = Button(image=right, highlightthickness=0, command=known)
correct.grid(row=1, column=1)

incorrect = Button(image=wrong, highlightthickness=0, command=next_word)
incorrect.grid(row=1, column=0)

next_word()

window.mainloop()