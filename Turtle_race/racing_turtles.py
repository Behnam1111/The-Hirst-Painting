from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_choice = screen.textinput(title="Who will win?", prompt="Which turtle will win the race? choose a color")
is_race_on = True
color = ["red", "yellow", "blue", "green", "purple", "orange"]
y_positions = [0, -30, -60, -90, 30, 60, 90]
all_turtles = []
for turtle_index in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-235, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_choice:
                print(f"you win! The {winning_color} turtle won")
            else:
                print(f"you lost! , The {winning_color} turtle won")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
