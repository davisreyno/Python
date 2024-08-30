# Objectives:
    # Create a snake body
    # Move the snake
    # Control the snake with key bindings
    # Detect collision with food
    # Create a scoreboard
    # Detect collision with wall
    # Detect collision with tail

# See turtle documentation at https://docs.python.org/3/library/turtle.html#color-control

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("grey")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard() 

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food, distaqnce() from Turtle 
    if snake.head.distance(food) < 13:
        food.refresh() 
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall. Game over. 
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False 
        scoreboard.game_over()

    # Detect collision with tail. Game over. 
    for segment in snake.segment[1:]): 
        if snake.head.distance(segment) < 10: 
            game_is_on = False 
            scoreboard.game_over() 

screen.exitonclick()
