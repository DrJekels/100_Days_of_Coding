import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "indigo"]
y_position = [-70, -40, -10, 20, 50, 80]
turtles = []

for turtle in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle])
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet.lower():
                print(f"Your turtle won! The {winning_color} turtle is the winner!")
            else:
                print(f"Your tutle lost. The {winning_color} turtle is the winner!")
            is_race_on = False
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()