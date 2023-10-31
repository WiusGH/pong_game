from turtle import Screen
from board_lines import ScreenDivisor
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
# Screen related
game_is_on = True
screen = Screen()
screen.bgcolor('black')
screen.setup(width=1000, height=600)
screen.tracer(0)
screen_divisor = ScreenDivisor()
screen.title('Pong')
screen.listen()
# Paddles related
l_paddle = Paddle(-480, 0)
r_paddle = Paddle(473, 0)
# Ball related
ball = Ball()
# Scoreboard related
scoreboard = Scoreboard()
# Keypress related
screen.onkeypress(l_paddle.move_up, 'w')
screen.onkeypress(l_paddle.move_down, 's')
screen.onkeypress(r_paddle.move_up, 'Up')
screen.onkeypress(r_paddle.move_down, 'Down')
# screen.onkey(scoreboard.reset_score(), 'r')
# Game functions
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Paddle bounce
    if ball.xcor() < -450 and ball.distance(l_paddle) < 60:
        ball.paddle_bounce()
    if ball.xcor() > 458 and ball.distance(r_paddle) < 60:
        ball.paddle_bounce()
    # Y bounce
    if ball.ycor() > 290 or ball.ycor() < -280:
        ball.bounce_y()
    # Scoring
    if ball.xcor() > 475:
        ball.reset_position()
        scoreboard.l_increase()
        scoreboard.update_scoreboard()
    if ball.xcor() < -485:
        ball.reset_position()
        scoreboard.r_increase()
        scoreboard.update_scoreboard()
screen.exitonclick()
