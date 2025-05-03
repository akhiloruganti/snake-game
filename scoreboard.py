from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.s=0
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.s}",align="center",font=("Arial",20,"normal"))
        self.hideturtle()
        #self.hide()
    def upda(self):
        self.s=self.s+1
        self.clear()
        self.write(f"Score: {self.s}",align="center",font=("Arial",20,"normal"))
    def game_over(self):
        self.goto(0,0)
        self.color('green')
        self.write(f"Game-Over ",align="center",font=("Arial",60,"normal"))
