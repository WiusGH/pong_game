from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-150, 200)
        self.write(arg=self.l_score, font=('arial', 60, 'bold'))
        self.goto(100, 200)
        self.write(arg=self.r_score, font=('arial', 60, 'bold'))

    def l_increase(self):
        self.clear()
        self.l_score += 1

    def r_increase(self):
        self.clear()
        self.r_score += 1

    # def reset_score(self):
    #     self.l_score = 0
    #     self.r_score = 0
    #     self.goto(-150, 200)
    #     self.clear()
    #     self.write(arg=self.l_score, font=('arial', 60, 'bold'))
    #     self.goto(100, 200)
    #     self.clear()
    #     self.write(arg=self.r_score, font=('arial', 60, 'bold'))

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', font=('arial', 12, 'bold'))
