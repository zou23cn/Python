guess = eval(input())

#单分支结构
if guess == 99:
    print("猜对了")
else:
    print("猜错了")

#二分支结果
print("猜{}了".format("对" if guess == 99 else "错"))


#多分支结构
score = eval(input())
if score >= 60:
    grade = "D"
elif score >= 70:
    grade = "C"
elif score >= 80:
    grade = "B"
elif score >= 90:
    grade = "A"
else:
    grade = "E"
print("输入成绩属于级别{}".format(grade))
