from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x, y)

    def move_up(self):
        new_y = self.ycor() + 30
        if self.ycor() < 260:
            self.sety(new_y)

    def move_down(self):
        new_y = self.ycor() - 30
        if self.ycor() > -260:
            self.sety(new_y)
