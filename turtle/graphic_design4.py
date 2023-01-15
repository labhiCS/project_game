from turtle import *
from colorsys import *

pensize(4)
h = 0.4
for i in range(180, 30, -30):
    c = hsv_to_rgb(h, 1, 1)
    color("black")
    fillcolor(c)

    begin_fill()
    for j in range(6):
        for k in range(6):
            h += 0.005
            fd(i)
            lt(60)
        lt(60)
    end_fill()
    
done()