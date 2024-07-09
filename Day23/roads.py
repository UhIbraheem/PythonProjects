from turtle import Turtle

MAX_Y = 170
ROAD_WIDTH = 30


class Roads(Turtle):

    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.penup()
        self.shape("turtle")
        self.setheading(180)
        self.color("grey")
        self.are_on = False
        self.crossed_line = False
        self.x = 300
        self.y = -220

    def won(self):
        if self.ycor() > MAX_Y:
            self.crossed_line = True
        else:
            self.crossed_line = False

    def draw_lines(self):
        if self.ycor() < MAX_Y:
            self.showturtle()
            self.color("grey")
            self.goto(self.x, self.y)
            for i in range(30):
                self.pendown()
                self.forward(10)
                self.penup()
                self.forward(10)
                if i % 5 == 0:
                    self.screen.update()
            self.y += ROAD_WIDTH
        else:
            self.goto(self.x, self.y)
            self.color("red")
            for i in range(30):
                self.pendown()
                self.forward(10)
                self.penup()
                self.forward(10)
                if i % 3 == 0:
                    self.screen.update()
            self.hideturtle()
            self.are_on = True

    def erase(self):
        self.clear()
        self.x = 300
        self.y = -220
        self.goto(self.x, self.y)
        self.are_on = False
