from turtle import Turtle
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
DOWN=270
UP=90
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        self.body=[]
        self.createbody()
        self.head=self.body[0]
    def createbody(self):
        for i in STARTING_POSITIONS:
            body=Turtle("square")
            body.color("WHITE")
            body.penup()
            body.setposition(i)
            self.body.append(body)
    def addpart(self,position):
        newbody=Turtle("square")
        newbody.color("WHITE")
        newbody.penup()
        newbody.goto(position)
        self.body.append(newbody)
    def extend(self):
        self.addpart(self.body[-1].position())

    def move(self):
         
         for i in range(len(self.body)-1,0,-1):
            now=self.body[i-1].pos()
            self.body[i].goto(now)
         self.body[0].forward(20)
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(90)
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(180)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(0)