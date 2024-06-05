# Working with the turtle top create randomized art
import turtle as t
from random import choice, randint

# Creating the turtle class
tim = t.Turtle()
# Changing the shape of the turtle into a turtle shape
tim.shape("turtle")
t.colormode(255)


def random_color():
    x, y, z = randint(0, 255), randint(0, 255), randint(0, 255)
    color = (x, y, z)
    return color


circle = 360
tim.speed(0)
heading = 0
for i in range(circle // 4):
    heading += 4
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(heading)

# creating the screen and making it exit on click
screen = t.Screen()
screen.exitonclick()
