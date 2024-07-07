from random import choice
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_X = 320
ENDING_X = -320
Y_POSITIONS = [-205, -175, -145, -115, -85, -55, -25, 5, 35, 65, 95, 125, 155, 185]


class CarManager(Turtle):

    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.penup()
        self.setheading(180)
        self.shape("square")
        self.shapesize(1, 2)
        self.color(choice(COLORS))
        self.x = STARTING_X
        self.y = choice(Y_POSITIONS)
        self.starting_pos()
        self.speed = STARTING_MOVE_DISTANCE

    def drive(self):
        if self.xcor() > ENDING_X:
            self.forward(self.speed)
            self.screen.update()
        else:
            self.setpos(STARTING_X, self.y)

    def starting_pos(self):
        self.goto(self.x, self.y)
