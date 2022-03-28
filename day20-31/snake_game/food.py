import random
from turtle import Turtle
import random

MAX_POSITION = 290
MIN_POSITION = -290

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        random_x = random.randint(MIN_POSITION, MAX_POSITION)
        random_y = random.randint(MIN_POSITION, MAX_POSITION)
        self.goto(random_x, random_y)
