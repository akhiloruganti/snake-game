from turtle import Turtle,Screen
import time
from snakegame.snake import Snake
from snakegame.food import Food
from snakegame.scoreboard import ScoreBoard
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("snake Game")
screen.tracer(0)
score=ScoreBoard()
snake=Snake()
food=Food()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

run=True
while run:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food)<13:
        food.refresh()
        score.upda()
        snake.extend()

    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()<-290 or snake.head.ycor()>290:
        score.game_over()
        run=False
      

    






screen.exitonclick()
