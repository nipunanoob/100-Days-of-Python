import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

WIDTH = 600
HEIGHT = 600
FINISH_LINE_Y = 280
tick = 0
FONT = ("Courier", 24, "normal")

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)

screen.listen()

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.onkeypress(fun=player.move, key='Up')

def game_over():
    end = Turtle()
    end.hideturtle()
    end.write("GAME OVER!", align='center', font=FONT)

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    if tick % 5 == 0:
        car_manager.create_car()

    tick += 1
    car_manager.move_cars()
    screen.update()

    if player.ycor() >= FINISH_LINE_Y:
        scoreboard.increment_level()
        player.reset_turtle_position()
        car_manager.remove_all_cars()
        car_manager.increment_speed()
        tick = 0

    for car in car_manager.all_cars:
        if car.distance(player) <= 30:
            player.die()
            car_manager.stop_car_movement()
            game_over()
            screen.update()
            game_is_on = False

screen.exitonclick()



