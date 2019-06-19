#计算日期、天数
import time
import datetime

d1=datetime.date(2019,12,31)
d2=datetime.date(2019,5,7)
d3=d1-d2
print(d3)

print(10/365*d3)