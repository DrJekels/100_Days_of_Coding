import time

from turtle import Screen

from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

paddle_1 = Paddle(350)
screen.onkeypress(paddle_1.go_up, "Up")
screen.onkeypress(paddle_1.go_down, "Down")

paddle_2 = Paddle(-350)
screen.onkeypress(paddle_2.go_up, "w")
screen.onkeypress(paddle_2.go_down, "s")

ball = Ball()
scoreboard = ScoreBoard()

game_on = True
while game_on:
    
    time.sleep(ball.move_speed())
    screen.update()
    ball.move()
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    
    if ball.xcor() > 340 and ball.distance(paddle_1) < 50 or ball.xcor() < -340 and ball.distance(paddle_2) < 50:
        ball.block()

    if ball.xcor() > 380:
        scoreboard.update_scoreL()
        ball.reset_position()

    if ball.xcor() < -380:
        scoreboard.update_scoreR()
        ball.reset_position()

screen.exitonclick()