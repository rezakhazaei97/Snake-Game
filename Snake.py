from turtle import Turtle

snakeBodyPosStart = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class snake:

    def __init__(self):
        self.snakeBodyList = []
        for pos in snakeBodyPosStart:
            self.createBody(pos)

    def createBody(self,pos):
        newSnakeBody = Turtle("square")
        newSnakeBody.color("white")
        newSnakeBody.penup()
        newSnakeBody.setposition(pos)
        self.snakeBodyList.append(newSnakeBody)

    def addTile(self):
        self.createBody(self.snakeBodyList[-1].position())

    def move(self):
        for i in range(len(self.snakeBodyList) - 1, 0, -1):
            x = self.snakeBodyList[i - 1].xcor()
            y = self.snakeBodyList[i - 1].ycor()
            self.snakeBodyList[i].goto(x, y)

        self.snakeBodyList[0].forward(20)

    def up(self):
        if self.snakeBodyList[0].heading() != DOWN:
            self.snakeBodyList[0].setheading(90)

    def down(self):
        if self.snakeBodyList[0].heading() != UP:
            self.snakeBodyList[0].setheading(270)

    def left(self):
        if self.snakeBodyList[0].heading() != RIGHT:
            self.snakeBodyList[0].setheading(180)

    def right(self):
        if self.snakeBodyList[0].heading() != LEFT:
            self.snakeBodyList[0].setheading(0)
