from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, x, y):
        super(Scoreboard, self).__init__()
        self.color('white')
        self.penup()
        self.goto(x, y)
        self.score = 0
        self.hideturtle()
        self.write(f"{self.score}", align='center', font=('Courier', 64, 'normal'))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", align='center', font=('Courier', 64, 'normal'))

