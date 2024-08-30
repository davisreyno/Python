from turtle import Turtle 
import random 

# Class inheritance 

class Food(Turtle): 

    def __init__(self):
        super().__init__() 
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("black")
        self.speed("fastest")
        self.refresh() 

        # Food moves to (new) random location, upon collision 

    def refresh(self): 
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

