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
cars = []
for i in range(25):
    car = CarManager(screen)
    cars.append(car)

screen.listen()
screen.onkey(player.move, "w")

game_is_on = True
while game_is_on:
    screen.update()
    roads.draw_lines()

    if roads.are_on:
        for car in cars:
            car.drive()
            screen.update()
            if car.collision_range(player):
                scoreboard.game_over()
                game_is_on = False

    if player.ycor() > 230:
        player.level_up()
        scoreboard.point()
        for car in cars:
            car.starting_pos()
            car.increase_speed()
        roads.erase()

    time.sleep(0.05)

screen.exitonclick()
