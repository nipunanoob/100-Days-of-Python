import random
import turtle as t

tim = t.Turtle()

tim.speed('fastest')
screen = t.Screen()
screen.colormode(255)
degree = 0
size_of_gap = 5

for i in range(int(360 / size_of_gap)):
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    tim.pencolor((R, G, B))
    tim.circle(150)
    tim.left(size_of_gap)

screen.exitonclick()
