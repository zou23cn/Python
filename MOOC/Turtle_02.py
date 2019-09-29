import turtle
colors = ["red","yellow","purple","blue"]
turtle.screensize(800,600,"white")
turtle.pencolor("red")
turtle.circle(100)
for i in range(12):
    turtle.circle(100,steps = 3)
    turtle.color(colors[i % 4])
    turtle.circle(100,10)
turtle.done()