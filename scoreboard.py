from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.show_score()

    def show_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=self.l_score, align='center', font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(arg=self.r_score, align='center', font=('Courier', 80, 'normal'))

    def increase_lscore(self):
        self.l_score += 1
        self.show_score()

    def increase_rscore(self):
        self.r_score += 1
        self.show_score()

