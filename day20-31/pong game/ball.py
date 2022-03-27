import random
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__(shape="circle")
        self.color('white')
        self.penup()
        self.x_move = random.choice([10, -10])
        self.y_move = random.choice([10, -10])

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def hit(self):
        self.x_move *= -(random.random() + 1)

    def reset(self):
        self.goto(0, 0)
        self.x_move = random.choice([10, -10])
        self.y_move = random.choice([10, -10])

