#正方形画图
import turtle
for i in range(360):
    turtle.seth(i)
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)