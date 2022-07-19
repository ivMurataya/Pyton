from turtle import  Turtle
ALIGMENT = 'center'
FONT = ("Arial", 8, "normal")

class Names(Turtle):
    def __init__(self, name,Xcor, Ycor):
        super().__init__()
        self.penup()
        self.State = name
        self.X = Xcor
        self.Y = Ycor
        self.hideturtle()
        self.update()
    def update(self):
        self.clear()
        self.goto(self.X,self.Y)
        self.write(f"{self.State}", True,ALIGMENT , FONT)