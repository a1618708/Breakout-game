from turtle import Turtle

ROW = 7


class Block():
    def __init__(self):
        self.create_blocks()

    def create_blocks(self):
        self.blocks = []
        colors = ["#02475E", "#687980", "#F3BDA1", "#FEFECC"]
        initial_x = - 267
        initial_y = + 200
        for j in range(ROW):
            for i in range(9):
                block = Turtle("square")
                block.color(colors[(i+j)%4])
                block.shapesize(1,3)
                block.penup()
                block.setpos(initial_x+66*i, initial_y)
                self.blocks.append(block)
            initial_y -= 25
        self.blocks.reverse()

