from turtle import Turtle
FONT = ("Courier", 24, "normal")
TEXT_POSITION = (-280, 260)





class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.penup()
        self.hideturtle()
        self.goto(TEXT_POSITION)
        self.level = 1
        self.write(f"Level: {self.level}", move=False, font=FONT)

    def increment_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", move=False, font=FONT)

