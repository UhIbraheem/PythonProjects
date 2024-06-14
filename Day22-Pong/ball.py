from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 0.01

    def move_ball(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.setpos(x, y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_ball(self):
        self.goto(0, 0)
        self.move_speed = 0.01
        self.bounce_x()
