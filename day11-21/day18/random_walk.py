import random
from turtle import Turtle

timmy = Turtle()
timmy.width(10)
timmy.speed('fastest')
while True:
    R = random.random()
    G = random.random()
    B = random.random()
    direction = random.randint(1, 4)
    timmy.color((R, G, B))
    if direction == 1:
        timmy.forward(25)
    elif direction == 2:
        timmy.left(90)
    elif direction == 3:
        timmy.right(90)
    else:
        timmy.backward(25)

