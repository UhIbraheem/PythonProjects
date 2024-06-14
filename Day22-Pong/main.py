from turtle import Screen
from time import sleep
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

LEFT_PADDLE = (-350, 0)
RIGHT_PADDLE = (350, 0)


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle(LEFT_PADDLE)
r_paddle = Paddle(RIGHT_PADDLE)

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

screen.onkey(r_paddle.go_up, "o")
screen.onkey(r_paddle.go_down, "l")

game_on = True
x_count = y_count = 0

while game_on:
    sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    # Detect collision with roof or floor
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 55 and ball.xcor() < -330:
        ball.bounce_x()

    #  Detect right miss
    if ball.xcor() > 400:
        scoreboard.l_point()
        ball.reset_ball()
        sleep(1)

    # detect left miss
    if ball.xcor() < -400:
        scoreboard.r_point()
        ball.reset_ball()
        sleep(1)


screen.exitonclick()
