from turtle import Turtle
class Paddle(Turtle):

    def __init__(self, x_position, y_position):
        super().__init__()
        self.create_paddle(x_position, y_position)

    def create_paddle(self, x_position,y_position):
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(x_position, y_position)
        self.speed("fastest")

    def go_up(self):
        new_ycor = self.ycor() + 20
        self.goto(self.xcor(), new_ycor)

    def go_down(self):
        new_ycor = self.ycor() - 20
        self.goto(self.xcor(), new_ycor)
