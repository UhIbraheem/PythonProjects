from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# Creating a snake body
snake_body = []
positions = [(0, 0), (-20, 0), (-40, 0)]
for position in positions:
    new_body = Turtle("square")
    new_body.color("white")
    new_body.setpos(position)
    snake_body.append(new_body)

screen.exitonclick()
