from os import stat
from tkinter import *

from numpy import string_
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzlet")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(
                150,
                125,
                width=280,
                text='Some question text',
                fill=THEME_COLOR,
                font=('arial', 20, 'italic')
            )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        check_image = PhotoImage("images/true.png")
        cross_image = PhotoImage("images/false.png")

        self.check = Button(image=check_image, highlightthickness=0, command=self.true_answer)
        self.check.grid(row=2, column=0)
        self.cross = Button(image=cross_image, highlightthickness=0, command=self.false_answer)
        self.cross.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score.config(text=f"Score: {self.quiz.score}")
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.check.config(state="disabled")
            self.cross.config(state="disabled")

    def true_answer(self):
        self.feedback(self.quiz.check_answer("True"))

    def false_answer(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)