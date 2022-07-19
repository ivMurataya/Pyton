from turtle import  Turtle
TOP = (280,280)
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 15
        self.y_move = 15
    def move(self):
        #while self.xcor() < 280 and self.ycor() < 280:
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)
    def bounceY(self):
        # self.x_move *= -1
        self.y_move *= -1
    def bounceX(self):
        self.x_move *= -1
    def resetPos(self):
        self.goto(0,0)
