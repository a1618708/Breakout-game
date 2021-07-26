from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(230,230)
        self.score = 0
        self.write(f"Score : {self.score}", align="center", font=("Arial", 14, "normal"))

    def add_score(self):
        self.clear()
        self.write(f"Score : {self.score}", align="center", font=("Arial", 14, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 14, "normal"))

    def game_end(self):
        self.goto(0, 0)
        self.write("You win!!", align="center", font=("Arial", 14, "normal"))