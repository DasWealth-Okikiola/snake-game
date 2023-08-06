from turtle import Turtle
goto = [(0, 0), (-20, 0), (-40, 0)]
move_by = 20
up = 90
down = 270
left = 180
right = 0


class Snake:
    # Turtle's attributes

    def __init__(self):
        self.full_line = []
        self.create()
        self.head = self.full_line[0]
        self.move_snakes()

# creating 3 turtles by looping through set positions

    def create(self):
        for place in goto:
            self.add_line(place)

# Function for creating turtle

    def add_line(self, place):
        line = Turtle(shape="square")
        line.penup()
        line.color("blue")
        line.goto(place)
        self.full_line.append(line)

# Reset the snake on every round
    def reset(self):
        for line in self.full_line:
            line.goto(x=7000, y=7500)
        self.full_line.clear()
        self.create()
        self.head = self.full_line[0]
# The extending turtle function

    def extend(self):
        self.add_line(self.full_line[-1].position())

# Aligning the snakes and making them move in order

    def move_snakes(self):
        for line in range(len(self.full_line) - 1, 0, -1):
            ex = self.full_line[line - 1].xcor()
            yy = self.full_line[line - 1].ycor()
            self.full_line[line].goto(ex, yy)
        self.head.forward(move_by)

# Functions for controlling the snake

    def up(self):
        if self.head.heading() != down:
            self.head.seth(up)

    def down(self):
        if self.head.heading() != up:
            self.head.seth(down)

    def left(self):
        if self.head.heading() != right:
            self.head.seth(left)

    def right(self):
        if self.head.heading() != left:
            self.head.seth(right)
