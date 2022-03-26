from turtle import Turtle

DISTANCE = 20  # Distance between blocks and distance travelled by block is constant
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.blocks = []
        self.create_snake()
        self.head = self.blocks[0]

    def create_snake(self):
        for i in range(3):
            self.add_segment((-DISTANCE * i, 0))

    def add_segment(self, position):
        new_block = Turtle('square')
        new_block.penup()
        new_block.goto(position)
        new_block.color('white')
        self.blocks.append(new_block)

    def extend(self):
        self.add_segment(self.blocks[-1].position())

    def move(self):
        for block_num in range(len(self.blocks) - 1, 0, -1):
            new_x = self.blocks[block_num - 1].xcor()
            new_y = self.blocks[block_num - 1].ycor()
            self.blocks[block_num].goto(new_x, new_y)
        self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
