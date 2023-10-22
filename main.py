from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from boundary import Boundary
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))
ball = Ball()
scoreboard = ScoreBoard()
boundary_line = Boundary()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with the upper and lower walls
    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.y_bounce()

    # detect collision with the paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 350 or ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.x_bounce()

    # detect R paddle misses
    if ball.xcor() > 390:
        ball.reset()
        scoreboard.increase_lscore()

    # detect L paddle misses
    if ball.xcor() < -390:
        ball.reset()
        scoreboard.increase_rscore()


screen.exitonclick()
