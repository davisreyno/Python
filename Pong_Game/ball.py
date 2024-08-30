from turtle import Turtle 

class Ball(Turtle): 

    # Create ball 
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shapt("circle")
        self.penup() 

    # Move ball 
    def move(self):
        new_x = self.xcor() + 10 
        new_y = self.ycor + 10
        self.goto(new_x, new_y)