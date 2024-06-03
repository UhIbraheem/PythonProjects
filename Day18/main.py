# Working with the turtle top create randomized art
from turtle import Turtle, Screen
from random import choice
# Creating the turtle class
tim = Turtle()
# Changing the shape of the turtle into a turtle shape
tim.shape("turtle")


colors = ["sky blue", "grey", "red", "yellow", "green", "blue","black", "purple", "dark sea green", "salmon", "cyan4", "pink"]
direction = [0, 90, 180, 270]
tim.pensize(8)
n = 100
for i in range(n):
    tim.color(choice(colors))
    tim.forward(20)
    tim.setheading(choice(direction))


# creating the screen and making it exit on click
screen = Screen()
screen.exitonclick()
