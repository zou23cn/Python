import turtle as t

length = 0
# while (length <=400):    #利用正方形螺旋线的性质来绘图
for i in range(50):
    t.fd(length)
    t.left(90)
    length += 2
# t.hideturtle()         #绘图结束后把海龟头(笔触头)隐藏起来
t.done()               #绘图结束后使窗口停留
