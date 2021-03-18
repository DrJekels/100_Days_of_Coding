###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import turtle
import random

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

turtle.colormode(255)
tim = turtle.Turtle()

def draw(move, x, y):
    for i in range(x):
        for j in range(y):
            tim.pencolor(random.choice(rgb_colors))
            tim.dot()
            tim.forward(move)
        tim.backward(move*y)
        tim.left(90)
        tim.forward(move)
        tim.right(90)

tim.penup()
draw(10, 12, 10)