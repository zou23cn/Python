#六角形绘制
import turtle

for i in (270,210,150,90,30,-30):
    turtle.seth(i)
    turtle.fd(60)
    turtle.seth(i-120)
    turtle.fd(60)
    turtle.seth(i-240)
    turtle.fd(120)
   
turtle.done()