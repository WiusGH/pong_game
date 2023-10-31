from turtle import Turtle
import random
STARTING_SPEED = 10 * 2
SPEED_INCREASE = 0.9

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        random_heading = random.randint(0, 359)
        self.color('white')
        self.shape('circle')
        self.penup()
        self.x_move = STARTING_SPEED
        self.y_move = STARTING_SPEED
        self.move_speed = 0.05

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1
        self.move_speed *= SPEED_INCREASE

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.05
        self.paddle_bounce()
