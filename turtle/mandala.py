import turtle

t = turtle.Turtle()
l = ["Purple", "red", "orange", "blue", "green"]
turtle.bgcolor("black")

for i in range(200):
    t.speed(0)
    t.color(l[i%5])
    t.pensize(i/10+1)
    t.forward(i)
    t.left(59)

turtle.mainloop()