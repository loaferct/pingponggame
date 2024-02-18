from turtle import Screen
from paddle import Paddle
from ball import Ball
import time 

screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.goup, "Up")
screen.onkey(r_paddle.godown, "Down")
screen.onkey(l_paddle.goup, "w")
screen.onkey(l_paddle.godown, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

if ball.ycor()>280 or ball.ycor()<-280 :
    ball.bounce()

screen.exitonclick()