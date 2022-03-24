from turtle import Turtle, Screen

terry = Turtle()

for i in range(10):
    terry.forward(10)
    terry.penup()
    terry.forward(10)
    terry.pendown()

screen = Screen()
screen.exitonclick()
