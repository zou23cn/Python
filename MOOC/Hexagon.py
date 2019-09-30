#绘制六边形
import turtle
turtle.penup()
turtle.goto(-100,-200)
turtle.pendown()
turtle.pensize(5)
for i in range(6):
    turtle.fd(200)
    turtle.left(60)
turtle.done()