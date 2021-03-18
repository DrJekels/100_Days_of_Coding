import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_cars()

    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.gameover()
    
    if player.is_at_finish_line():
        cars.level_up()
        player.level_up()
        scoreboard.update_level()

screen.exitonclick()