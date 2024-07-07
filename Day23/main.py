import time
from roads import Roads
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
roads = Roads(screen)
car = CarManager(screen)
screen.listen()
screen.onkey(player.move, "w")

game_is_on = True
while game_is_on:
    roads.draw_lines()
    if roads.are_on:
        car.drive()
    time.sleep(0.05)
    screen.update()



screen.exitonclick()
