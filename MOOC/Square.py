#绘制正方形
import turtle
turtle.penup()
turtle.goto(-100,-100)
turtle.pendown()
turtle.pensize(5)
for i in range(4):
    turtle.fd(200)
    turtle.left(90)
turtle.done()
