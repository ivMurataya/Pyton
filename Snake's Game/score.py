from turtle import  Turtle
ALIGMENT = 'center'
FONT = ("Arial", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.update()
        self.hideturtle()
        self.ReadHighScore()
    def update(self):
        self.clear()
        self.goto(0, 250)
        self.write(f"Score {self.points} High Score: {self.high_score}", True,ALIGMENT , FONT)
    def reset(self):
        if self.points > self.high_score:
            self.high_score = self.points
            self.WriteHighScore(self.high_score)
        self.points = 0
        self.update()

    def new_Point(self):
        self.points +=1
        self.update()

    def ReadHighScore(self):
        file = open("data.txt")
        self.high_score = int(file.read())
        self.update()
        file.close()
    def WriteHighScore(self,hs):
        with open("data.txt", mode="w") as file:
            points = str(hs)
            file.write(points)


