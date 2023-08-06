from turtle import Turtle
import random
color = ["red", "magenta", "orange", "blue", "white", "brown", "yellow", "purple", "grey", "green"]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.refresh()

    def refresh(self):
        self.color(random.choice(color))
        xa = random.randint(-270, 270)
        ya = random.randint(-270, 260)
        self.goto(x=xa, y=ya)
