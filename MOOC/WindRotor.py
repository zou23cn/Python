#绘制风轮
import turtle
turtle.pensize(5)
for i in range(4):
    turtle.fd(200)
    turtle.right(90)
    turtle.circle(-200,45)
    turtle.goto(0,0)
    turtle.left(45)
turtle.done()