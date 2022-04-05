from turtle import Turtle, Screen

turtle = Turtle()


def move_and_turn_left(pointer):
    pointer.forward(50)
    pointer.left(90)


for i in range(4):
    move_and_turn_left(turtle)

Screen().exitonclick()
