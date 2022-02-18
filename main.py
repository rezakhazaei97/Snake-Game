import turtle
from turtle import Screen
from Snake import snake
from Food import Food
from ScoreBord import scoreBord
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)
screen.bgcolor("black")

Snake = snake()
Food = Food()
Score = scoreBord()

screen.listen()
screen.onkey(Snake.up, "Up")
screen.onkey(Snake.down, "Down")
screen.onkey(Snake.left, "Left")
screen.onkey(Snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    Snake.move()
    if Snake.snakeBodyList[0].distance(Food) < 15:
        Score.clearScore()
        Score.score += 1
        Score.showScore()
        Snake.addTile()
        Food.ShowFood()

    if (Snake.snakeBodyList[0].xcor() > 290 or Snake.snakeBodyList[0].xcor() < -290 or Snake.snakeBodyList[0].ycor() > 290 or Snake.snakeBodyList[0].ycor() < -290 ):
        game_is_on = False
        Score.gameOver()

    for tile in Snake.snakeBodyList[1:]:
        if Snake.snakeBodyList[0].distance(tile) < 10:
            game_is_on = False
            Score.gameOver()


screen.exitonclick()
