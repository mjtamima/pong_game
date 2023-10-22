from turtle import Turtle
START = -300
STOP = 300
SKIP = 25

class Boundary():

    def __init__(self):
        self.create_line()

    def create_line(self):
        for pos in range(START, STOP, SKIP):
            new_part = Turtle('square')
            new_part.shapesize(stretch_wid=0.5, stretch_len=0.1)
            new_part.color('white')
            new_part.penup()
            new_part.goto(0, pos)
