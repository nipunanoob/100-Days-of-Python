import time
from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard

RIGHT_DOWN_WALL_LIMIT = 280
UP_LEFT_WALL_LIMIT = 300

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="w", fun=snake.up)
screen.onkey(key="s", fun=snake.down)
screen.onkey(key="a", fun=snake.left)
screen.onkey(key="d", fun=snake.right)

is_running = True
while is_running:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.score += 1
        scoreboard.update_score()
        snake.extend()

    if snake.head.xcor() > RIGHT_DOWN_WALL_LIMIT\
            or snake.head.xcor() < -UP_LEFT_WALL_LIMIT\
            or snake.head.ycor() > UP_LEFT_WALL_LIMIT\
            or snake.head.ycor() < -RIGHT_DOWN_WALL_LIMIT:
        scoreboard.reset()
        snake.reset()

    for block in snake.blocks[1:]:
        if snake.head.distance(block) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
