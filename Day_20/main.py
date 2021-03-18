import time
from turtle import Turtle, Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0, 0)

snake = Snake()

screen.listen()
screen.onkey(snake.up(), "w")
screen.onkey(snake.down(), "s")
screen.onkey(snake.right(), "d")
screen.onkey(snake.left(), "a")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()