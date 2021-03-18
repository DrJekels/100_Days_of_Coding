from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", move=False, align="center", font=("Courier", 10, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", move=False, align="center", font=("Courier", 10, "normal"))
    
    def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))