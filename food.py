from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("orange")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.refresh()

    def refresh(self):
        x_position = random.randint(-280, 280)
        y_position = random.randint(-280, 280)
        self.goto(x_position, y_position)
