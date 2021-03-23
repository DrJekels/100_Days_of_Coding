import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer", font=(FONT_NAME, 34, "bold"), bg=YELLOW, fg=GREEN)
    check_mark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    for n in range(8):
        if n % 8 == 0:
            title.config(text="Break", font=(FONT_NAME, 34, "bold"), bg=YELLOW, fg=RED)
            count_down(LONG_BREAK_MIN*60)            
        elif n % 2 == 0:
            title.config(text="Break", font=(FONT_NAME, 34, "bold"), bg=YELLOW, fg=PINK)
            count_down(SHORT_BREAK_MIN*60)
        else:
            title.config(text="Work", font=(FONT_NAME, 34, "bold"), bg=YELLOW, fg=GREEN)
            count_down(WORK_MIN*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    min = math.floor(count/60)
    sec = count%60
    check = ""
    canvas.itemconfig(timer_text, text=f"{min:02d}:{sec:02d}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        check += "✓"
        check_mark.config(text=check)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

tomato_image = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

title = Label(text="Timer", font=(FONT_NAME, 34, "bold"), bg=YELLOW, fg=GREEN)
title.grid(column=1, row=0)

check_mark = Label(font=(FONT_NAME, 10, "bold"), bg=YELLOW, fg=GREEN)
check_mark.grid(column=1, row=3)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()