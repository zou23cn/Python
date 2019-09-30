from turtle import *
fillcolor("red")
begin_fill()
while True:
    forward(100)
    right(-60)
    forward(100)
    right(120)
    if abs(pos()) < 1:
        break
end_fill()

done()