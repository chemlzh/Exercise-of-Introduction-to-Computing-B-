import turtle
t=turtle.Pen()
pad=turtle.Screen()
colors=["red", "yellow", "blue", "green", "orange","purple", "white", "gray", "brown", "sea green"]
pad.bgcolor("black")
t.speed(100)
edge=int(input())
for x in range(1000):
    t.color(colors[(x-1)%edge])
    t.pensize(x//100+1)
    t.forward(x)
    t.left(360/edge+1)
pad.exitonclick()