from turtle import Screen
from paddle import Paddle
from ball import Ball
import time 
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.goup, "Up")
screen.onkey(r_paddle.godown, "Down")
screen.onkey(l_paddle.goup, "w")
screen.onkey(l_paddle.godown, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #bounce ball from top and bottom
    if ball.ycor()>260 or ball.ycor()<-260 :
        ball.bounce_y()

    #detect collisions with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #right paddle miss detection
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        

    #left paddle miss detection
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        

screen.exitonclick()