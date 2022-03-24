import random
import turtle
from turtle import Turtle, Screen
from random import random

tony = Turtle()

for num_of_sides in range(3, 11):
    angle = 360 / num_of_sides
    R = random()
    B = random()
    G = random()
    tony.pencolor(R, G, B)
    for sides in range(0, num_of_sides):
        tony.forward(100)
        tony.left(angle)

screen = Screen()
screen.exitonclick()
