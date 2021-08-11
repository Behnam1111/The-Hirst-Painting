from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_choice = screen.textinput(title="Who will win?", prompt="Which turtle will win the race? choose a color")
color = ["red", "yellow", "blue", "green", "purple", "orange"]
y_positions = [0, -30, -60, -90, 30, 60, 90]
for turtle_index in range(0, 5):
    tim = Turtle(shape="turtle")
    tim.color(color[turtle_index])
    tim.penup()
    tim.goto(x=-235, y=y_positions[turtle_index])

screen.exitonclick()
