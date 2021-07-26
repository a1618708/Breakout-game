from turtle import Screen
from paddle import Paddle
from block import Block
from ball import Ball
from score_board import ScoreBoard
import time
screen = Screen()
screen.title("Breakout Game")
screen.bgcolor("black")
screen.setup(width=600, height=500)
screen.tracer(0) #set with screen.update()
paddle = Paddle()
block = Block()
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(paddle.move_left, "Left")
screen.onkeypress(paddle.move_right, "Right")


Game_Over = False
Start = False
while not Game_Over:
    time.sleep(0.05)
    screen.update()
    if not Start:
        time.sleep(0.5)
        Start = True
    ball.move()


    if ball.xcor() >= 290 or ball.xcor() <= -290:
        ball.collide_sidewall()
    elif ball.ycor() >= 240:
        ball.collide_upperwall()
    elif -190 <= ball.ycor() <= -180 and ball.distance(paddle) <= 50:
        ball.collide_upperwall()
    elif ball.ycor() < -210:
        scoreboard.game_over()
        Game_Over = True

    for block1 in block.blocks:
         if abs(ball.ycor()-block1.ycor()) <= 10 and abs(ball.xcor()-block1.xcor()) <= 28:
            block1.color("black")
            block.blocks.remove(block1)
            scoreboard.score += 1
            scoreboard.add_score()
            if block.blocks == [] :
                scoreboard.game_end()
                Game_Over = True
            elif 0 <= (ball.xcor()-(block1.xcor()+30)) <= 5:
                ball.collide_sidewall()
            elif 0 >= (ball.xcor()-(block1.xcor()-30)) >= -5:
                ball.collide_sidewall()
            elif abs(ball.ycor()-block1.ycor()) <= 10:
                ball.collide_upperwall()


screen.exitonclick()
