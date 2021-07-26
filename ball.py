from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.8, 0.8)
        self.penup()
        self.color("white")
        self.goto(0, -180)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def collide_sidewall(self):
        self.x_move *= -1

    def collide_upperwall(self):
        self.y_move *= -1

