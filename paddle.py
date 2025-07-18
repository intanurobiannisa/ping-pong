from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        # self.hideturtle()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        # self.speed("fastest")
        self.goto(position)
        # self.showturtle()

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

