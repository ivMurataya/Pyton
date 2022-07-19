import time
from food import Food
from score import Score
from turtle import Turtle, Screen
from snake import  Snake

sc = Screen()
sc.setup(600,600)
sc.bgcolor("black")
sc.title("Snake Game")
sc.tracer(0)

snake = Snake()
food = Food()
score = Score()


sc.listen()
sc.onkey(snake.up,"Up")
sc.onkey(snake.down,"Down")
sc.onkey(snake.left,"Left")
sc.onkey(snake.right,"Right")

gameon = True
while gameon:
    sc.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.new_Point()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280or  snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <10:
            score.reset()
            snake.reset()


sc.exitonclick()
