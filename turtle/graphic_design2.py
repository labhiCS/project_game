from turtle import *

bgcolor("black")
pencolor("blue")
pensize(3)
speed(0)

for i in range(0, 1002):
    fd(8)
    seth(360*pow(i,3)/1002)

done()