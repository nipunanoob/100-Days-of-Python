from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10



class Player(Turtle):
    def __init__(self):
        super().__init__(shape='turtle')
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reset_turtle_position(self):
        self.goto(STARTING_POSITION)

    def die(self):
        self.hideturtle()


