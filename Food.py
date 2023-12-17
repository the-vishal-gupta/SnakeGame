import turtle
from turtle import Turtle
import random

turtle.colormode(255)

color_list = ["red", "green", "blue", "white", "purple", "pink", "orange"]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.color(random.choice(color_list))
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)
