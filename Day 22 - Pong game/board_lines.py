from turtle import Turtle

line_pos = 250


class ScreenDivisor(Turtle):
    def __init__(self):
        y_axis = 279
        super().__init__()
        for lines in range(12):
            self.divisor = Turtle()
            self.divisor.shape('square')
            self.divisor.penup()
            self.divisor.color('white')
            self.divisor.shapesize(stretch_len=0.1, stretch_wid=1.5)
            self.divisor.goto(x=0, y=y_axis)
            y_axis -= 50
