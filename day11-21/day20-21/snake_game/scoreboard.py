from turtle import Turtle

location = (0, 265)
FONT = ('Courier', 24, 'normal')
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(location)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)
