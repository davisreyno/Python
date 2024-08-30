# Objectives:
# Create the screen 
# Create and move a paddle 
# Create another paddle 
# Create the ball and make it move 
# Detect collision with the wall and bounce 
# Detect collision with paddle 
# Detect when paddle misses 
# Keep score 

from turtle import Screen, Turtle  
from paddle import Paddle 

# Create a screen 
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0) # Turns of animation but will need refresh with screen.update() 

# Create left and right paddle 
r_paddle = Paddle((350, 0))
l_paddle = Paddle(-350, 0)

# Move paddles 
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True 
while game_is_on: 
    screen.update() 

screen.exitonclick()
