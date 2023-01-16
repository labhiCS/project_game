from turtle import *
from colorsys import*
bgcolor("black")
speed(0)
pensize(4)
h = 0
for i in range(550):
    c = hsv_to_rgb(h, 1, 1)
    color(c)
    h += 0.005
    circle(200-i, 25)
    lt(220)
    circle(200-i, 25)
    lt(40)
done()