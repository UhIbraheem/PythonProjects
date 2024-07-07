from turtle import Turtle

STARTING_POSITION = (0, -270)
MOVE_DISTANCE = 30
FINISH_LINE_Y = 230


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shape("turtle")
        self.color("black")
        self.setpos(STARTING_POSITION)
        self.score = 0
        self.level_up()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def level_up(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.score += 1
