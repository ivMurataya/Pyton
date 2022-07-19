START_POS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
from  turtle import Turtle
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        for pos in START_POS:
            self.add_segment(pos)

    def add_segment(self, position):
        newSegment = Turtle()
        newSegment.shape("square")
        newSegment.color("white")
        newSegment.penup()
        newSegment.goto(position)
        self.segments.append(newSegment)
    def extend(self):
        self.add_segment(self.segments[-1].position())
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            newX = self.segments[seg_num - 1].xcor()
            newY = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(newX, newY)
        self.head.fd(MOVE_DISTANCE)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

