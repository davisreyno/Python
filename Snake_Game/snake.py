from turtle import Turtle

# Constants: Helps with coding flexibility for game creation
STARTING_POSITIONS = starting_positions = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# Class
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]  # Head of the snake

    # Creates three segment snake using START_POSITIONS
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position): 
        new_segment = Turtle("square")
        new_segment.color("black")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    #Add a new segment to snake after every food 
    def extend(self): 
        self.add_segment(self.segments[-1].position())


    # Moves snake
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heaing() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heaing() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heaing() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heaing() != LEFT:
            self.head.setheading(RIGHT)