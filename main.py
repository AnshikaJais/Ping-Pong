from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

screen.title("PING PONG BALL GAME")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
l_paddle = Paddle(-380, 0)
r_paddle = Paddle(380, 0)
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "W")
screen.onkey(l_paddle.go_down, "S")

game_is_on = True

while game_is_on:
    time.sleep(ball.spd)
    screen.update()
    ball.move()

    # Detect collision with top and bottom of the wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        # Needs to bounce
        ball.bounce_y()

    # Detect collision with r_paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 360:
        scoreboard.increase_rscore()
        ball.spd *= 0.9
        ball.bounce_x()

    # Detect collision with l_paddles
    if ball.distance(l_paddle) < 50 and ball.xcor() < -360:
        scoreboard.increase_lscore()
        ball.spd *= 0.9
        ball.bounce_x()

    # Detect collision with right wall
    if ball.xcor() > 385:
        ball.goto(0, 0)
        ball.spd = 0.1
        scoreboard.increase_lscore()
        ball.bounce_x()

    # Detect collision with left wall
    if ball.xcor() < -385:
        ball.goto(0, 0)
        ball.spd = 0.1
        scoreboard.increase_rscore()
        ball.bounce_x()

screen.exitonclick()
