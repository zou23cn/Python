#绘制叠边形
import turtle
turtle.penup()
turtle.goto(-100,-100)
turtle.pendown()
turtle.pensize(5)
for i in range(9):
    turtle.fd(200)
    turtle.left(80)
turtle.done()