from turtle import Turtle


class scoreBord(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

    def showScore(self):
        self.color("white")
        self.penup()
        self.setposition(0, 275)
        self.write(f"Score: {self.score}", align="center", font=('Arial', 15, 'normal'))
        self.hideturtle()

    def gameOver(self):
        self.goto(0,0)
        self.color("white")
        self.write("Game over", align="center", font=('Arial', 15, 'normal'))

    def clearScore(self):
        self.clear()
