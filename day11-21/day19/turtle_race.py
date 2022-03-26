import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Enter the color of turtle that will win the race: ")
colors = ['red', 'blue', 'green', 'orange', 'purple', 'maroon']
turtles = []
space = 50


for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-175+space)
    turtles.append(new_turtle)
    space += 50

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            if turtle.pencolor() == user_bet:
                print(f"You won $1,000,000 due to betting on {turtle.pencolor()}")
            else:
                print(f"You should have gone and bet on {turtle.pencolor()}")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
