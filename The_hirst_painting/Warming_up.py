from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
colours = ["red", "green", "yellow", "blue", "black", "purple", "orange", "gray"]
timmy.pensize(10)
timmy.speed(9)
for i in range(0, 3000):
    angle = random.choice([0, 90, 180, 270])
    timmy.pencolor(random.choice(colours))
    timmy.forward(20)
    timmy.right(angle)

screen = Screen()
screen.exitonclick()
