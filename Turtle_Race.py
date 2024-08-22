# For Turtle graphic documentation see https://docs.python.org/3/library/turtle.html

# Object state - different attributes or "states" between objects
# Instances
# Turtle Coordinate System

from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

# Betting screen with .textinput(title, prompt)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# .goto method with Python Turtle coordinate system

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            win_color = turtle.pencolor()
            if win_color == user_bet:
                print(f"You've won! The {win_color} turtle is the winner!")
            else:
                print(f"You've lost... the {win_color} turtle was the winner.")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
