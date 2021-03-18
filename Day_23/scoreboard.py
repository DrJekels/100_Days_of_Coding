from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-215, 260)
        self.write(f"Level: {self.level}", move=False, align="center", font=FONT)

    def update_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", move=False, align="center", font=FONT)

    def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)