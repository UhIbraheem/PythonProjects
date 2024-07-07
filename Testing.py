import time
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)

tim = Turtle()

tim.xcor = -250


for i in range(30):
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)


screen.exitonclick()
