from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.create_lscore()
        self.create_rscore()

    def create_lscore(self):
        self.goto(-100, 200)
        self.write(f"{self.l_score}",align= "center", font= ("Arial", 60,"normal"))

    def create_rscore(self):
        self.goto(100, 200)
        self.write(f"{self.r_score}", align="center", font=("Arial", 60, "normal"))

    def increase_lscore(self):
        self.clear()
        self.l_score += 1
        self.create_lscore()
        self.create_rscore()

    def increase_rscore(self):
        self.clear()
        self.r_score += 1
        self.create_lscore()
        self.create_rscore()
