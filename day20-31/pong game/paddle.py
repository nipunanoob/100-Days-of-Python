from turtle import Turtle

DISTANCE = 20
SPEED = 20
UP = 90
DOWN = 270
PADDLE_LENGTH = 3


class Paddle(Turtle):
    def __init__(self, pos):
        super(Paddle, self).__init__()
        self.blocks = []
        self.pos = pos
        self.create_paddle()
        self.pos = self.blocks[1].position()

    def create_paddle(self):
        for i in range(PADDLE_LENGTH):
            position_increment = (0, -DISTANCE * i)
            new_position = tuple(map(sum, zip(position_increment, self.pos)))
            self.add_block(new_position)

    def add_block(self, position):
        new_block = Turtle('square')
        new_block.penup()
        new_block.goto(position)
        new_block.color('white')
        self.blocks.append(new_block)

    def move_paddle_up(self):
        for block in self.blocks:
            current_position = block.position()
            new_position = current_position + (0, SPEED)
            block.setposition(new_position)
        self.pos = self.blocks[1].position()

    def move_paddle_down(self):
        for block in self.blocks:
            current_position = block.position()
            new_position = current_position + (0, -SPEED)
            block.setposition(new_position)
        self.pos = self.blocks[1].position()