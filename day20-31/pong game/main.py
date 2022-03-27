import time
from turtle import Screen, Turtle
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball

SCREEN_WIDTH = 850
SCREEN_HEIGHT = 600
DOTTED_LINE_SPACING = 10
PLAYER1_START_POSITION = (-(SCREEN_WIDTH - 50) / 2, 20)
PLAYER2_START_POSITION = ((SCREEN_WIDTH - 70) / 2, 20)

screen = Screen()
screen.tracer(0)
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title('My Pong Game')
screen.bgcolor('black')
screen.listen()
player1 = Paddle(PLAYER1_START_POSITION)
player2 = Paddle(PLAYER2_START_POSITION)
ball = Ball()
screen.onkeypress(key="w", fun=player1.move_paddle_up)
screen.onkeypress(key="s", fun=player1.move_paddle_down)
screen.onkeypress(key="Up", fun=player2.move_paddle_up)
screen.onkeypress(key="Down", fun=player2.move_paddle_down)
score1 = Scoreboard(-850//4, 200)
score2 = Scoreboard(850//4, 200)


def create_net():
    """ Creates vertical dashed line at middle of screen """
    pointer = Turtle()
    pointer.hideturtle()
    pointer.speed('fastest')
    pointer.penup()
    pointer.goto(0, -(SCREEN_HEIGHT - DOTTED_LINE_SPACING))
    pointer.setheading(90)  # Changes pointer to face North
    pointer.pendown()
    pointer.color('white')
    for i in range(SCREEN_HEIGHT // DOTTED_LINE_SPACING):
        pointer.forward(DOTTED_LINE_SPACING)
        pointer.penup()
        pointer.forward(DOTTED_LINE_SPACING)
        pointer.pendown()


create_net()
is_running = True

while is_running:
    time.sleep(0.1)
    screen.update()
    ball.move_ball()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if (ball.distance(player2.pos) < 50 and ball.xcor() > 370)\
            or (ball.distance(player1.pos) < 50 and ball.xcor() < -370):
        ball.hit()

    if ball.xcor() > 400:
        score1.update_score()
        ball.reset()

    if ball.xcor() < -400:
        score2.update_score()
        ball.reset()




screen.exitonclick()
