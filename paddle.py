from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("#0A81AB")
        self.shapesize(0.8,5)  #1 = 20px
        self.penup()
        self.goto(0, -200)


    def move_left(self):
        if self.xcor() > -240:
            self.setx(self.xcor()-20)

    def move_right(self):
        if self.xcor() < 240:
            self.setx(self.xcor()+20)






