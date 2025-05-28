from turtle import Turtle, Screen
import random

color_list = [(195, 177, 148), (159, 186, 177), (165, 184, 193), (198, 170, 180), (211, 196, 145), (205, 185, 184),
              (196, 204, 200), (221, 213, 215), (201, 186, 189), (185, 195, 192), (194, 198, 200), (187, 193, 195),
              (191, 191, 194), (131, 123, 112), (135, 129, 116), (137, 125, 120)]

tim = Turtle()
tim.shape("classic")
tim.color("black")
tim.hideturtle()
screen = Screen()
screen.colormode(255)
tim.speed(0)
tim.pu()
tim.setpos(-200, -200)
tim.pd()
y = 0
for j in range(10):
    for i in range(10):
        y = tim.ycor()
        tim.pd()
        tim.dot(20, random.choice(color_list))
        tim.pu()
        tim.forward(50)
        tim.pd()
    tim.pu()
    y = y + 50
    tim.setpos(-200, y)

screen.exitonclick()
