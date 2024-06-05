from turtle import Turtle, Screen

# program an etch sketch using the turtle library


tim = Turtle()
screen = Screen()
on = True


def move_forwards():
    tim.forward(30)


def move_backwards():
    tim.backward(30)


def rotate_counterclockwise():
    tim.left(10)


def rotate_clockwise():
    tim.right(10)


def clear():
    tim.reset()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=rotate_counterclockwise)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="c", fun=clear)


print("Thank you.")
screen.exitonclick()
