from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import  time
from score import Score
sc = Screen()
sc.setup(800,600)
sc.bgcolor("black")
sc.title("Pong Game")
sc.tracer(0)

R_pad = Paddle((380, 0))
L_pad = Paddle((-380, 0))
ball = Ball()
score = Score()

sc.listen()
sc.onkey(R_pad.up,"Up")
sc.onkey(R_pad.down,"Down")
sc.onkey(L_pad.up,"w")
sc.onkey(L_pad.down,"s")


game_is_on = True
flag = True
while game_is_on:
    time.sleep(0.05)
    sc.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceY()
    if (ball.distance(R_pad) < 60 and ball.xcor() > 350):
        ball.bounceX()
    if (ball.distance(L_pad) < 60 and ball.xcor() < -350):
        ball.bounceX()

    if ball.xcor() > 390:
        ball.bounceX()
        ball.resetPos()
        score.new_PointL()

    if  ball.xcor() < -390:
        ball.resetPos()
        ball.bounceX()
        score.new_PointR()
    if score.pointsL ==10 or score.pointsR ==10:
        ball.resetPos()
        score.gameover()
        game_is_on = False




sc.exitonclick()