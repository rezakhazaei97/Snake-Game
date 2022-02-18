from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        self.ShowFood()

    def ShowFood(self):
        foodX = random.randint(-280, 280)
        foodY = random.randint(-280, 280)
        self.goto(foodX, foodY)
