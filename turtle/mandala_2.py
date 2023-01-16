import turtle

t = turtle.Turtle()
l = ["red", "Green", "pink", "purple", "white"]
turtle.bgcolor("black")

for i in range(200):
    t.speed(0)
    t.color(l[i%5])
    t.pensize(i/50+1)
    t.forward(i)
    t.left(59)

turtle.mainloop()