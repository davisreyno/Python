
# Detect collision with the wall and bounce
# Detect collision with paddle
# Detect when paddle misses
# Keep score

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball 
import time

# Create a screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0) # Turns of animation but will need refresh with screen.update()

# Create left and right paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

# Move paddles
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect ball collision with wall & bounce
    if ball.ycor() > 280 or ball.ycor() < -280
        ball.bounce_y()

    # Detect collision with left and right paddles
    if ball.distance(r_paddle) < 50 and ball.xcor () > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
         

screen.exitonclick()
