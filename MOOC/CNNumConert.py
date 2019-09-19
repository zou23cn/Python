#ChiStr = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九']
ChiStr = "零一二三四五六七八九"
Num = input()

for i in Num:
    b = eval(i)
    print(ChiStr[b], end = '')