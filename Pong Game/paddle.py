from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, iPos):
        super().__init__()
        self.penup()
        self.goto(iPos)
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
    def up(self):
        new_y = self.ycor() +20
        self.goto(self.xcor(),new_y)
    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)



