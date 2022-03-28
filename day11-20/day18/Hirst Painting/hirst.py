# import colorgram
# colors = colorgram.extract('image.jpg', 30)
import random
import turtle
import turtle as t

t.colormode(255)
tim = t.Turtle()
screen = t.Screen()
screen.setworldcoordinates(-1, -1, screen.window_width() - 1, screen.window_height() - 1)
t.penup()
t.speed('fastest')


def draw_line(pointer, space, radius, color_list):
    for i in range(10):
        color = random.choice(color_list)
        pointer.dot(radius, color)
        if not i == 9:
            pointer.forward(space)
        else:
            pointer.left(90)
            pointer.forward(space)
            move_to_end_of_line(pointer)


def move_to_end_of_line(pointer):
    pointer.left(90)
    pointer.forward(450)
    pointer.left(180)


color_list = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157),
              (215, 74, 12), (15, 154, 16), (199, 14, 10), (243, 33, 165),
              (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61),
              (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214),
              (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40)]

for i in range(10):
    draw_line(t, 50, 20, color_list)
t.hideturtle()
screen.exitonclick()
