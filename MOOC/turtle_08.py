# 使用seth绘制三角形
import turtle
r = 0
for i in range(3):
    turtle.seth(r)
    turtle.fd(100)
    r+=120
turtle.done()
