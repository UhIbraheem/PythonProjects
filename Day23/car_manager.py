from random import choice
from turtle import Turtle

X_POSITIONS = []
for i in range(325, 901, 25):
    X_POSITIONS.append(i)

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 30
MOVE_INCREMENT = 7
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
        self.x = choice(X_POSITIONS)
        self.y = choice(Y_POSITIONS)
        self.starting_pos()
        self.speed = STARTING_MOVE_DISTANCE

    def drive(self):
        if self.xcor() > ENDING_X:
            self.forward(self.speed)
        else:
            self.setpos(choice(X_POSITIONS), choice(Y_POSITIONS))

    def starting_pos(self):
        self.goto(self.x, self.y)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT

    def collision_range(self, player):
        if (self.xcor() - 30 < player.xcor() < self.xcor() + 50) and (
                self.ycor() - 10 < player.ycor() < self.ycor() + 10):
            return True
        return False
