# 叠加等边三角形绘制
import turtle
# for i in range(3):
#     turtle.fd(100)
#     turtle.right(120)
# turtle.left(60)
# turtle.fd(100)
# for i in range(3):
#     turtle.right(120)
#     turtle.fd(200)
r = 0
for i in range(3):
    turtle.seth(r)
    turtle.fd(200)
    r+=120
turtle.seth(60)
turtle.fd(100)
r = 0
for i in range(3):
    turtle.seth(r)
    turtle.fd(100)
    r-=120

turtle.seth(0)   
turtle.done()