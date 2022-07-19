from turtle import  Turtle
ALIGMENT = 'center'
FONT = ("Arial", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.pointsR = 0
        self.pointsL = 0
        self.color("white")
        self.penup()
        self.update()
        self.hideturtle()
    def update(self):
        self.clear()
        self.goto(0, 250)
        self.write(f"{self.pointsL}        {self.pointsR}", True,ALIGMENT , FONT)
    def gameover(self):
        self.goto(0, 0)
        winner = ""
        if self.pointsR == 10:
            winner = "Left Player"
        elif self.pointsL ==10:
            winner = "Right Player"
        self.write(f"GAME OVER\n{winner} won!", True, ALIGMENT, FONT)

    def new_PointL(self):
        self.pointsL += 1
        self.update()
    def new_PointR(self):
        self.pointsR += 1
        self.update()


