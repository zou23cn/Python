import os
import time
path=r'd:\maillist.txt'
out_file = open(r"d:\sendlist.txt", 'w')
f1=open(path,'r')
patial_addr = []
i = 0
for line in f1.readlines():
    mailAddress = line.split('@')[1]# 截取拿到@符号后面的字符串
#print(mailAddress)# 163.com，qq.com
    if mailAddress.startswith('qq',0,2) or mailAddress.startswith('163',0,3) or mailAddress.startswith('126',0,3) or mailAddress.startswith('yahoo',0,5) or mailAddress.startswith('sina',0,4) or mailAddress.startswith('foxmail',0,7) or mailAddress.startswith('hotmail',0,7) or mailAddress.startswith('gmail',0,5) or mailAddress.startswith('outlook',0,7) or mailAddress.startswith('tom',0,3):
        pass
    else:
        patial_addr.insert(i, line.split('@')[1])
        i = i + 1
         # 获取其他邮箱类型

add = sorted(set(patial_addr), key = patial_addr.index)
n = len(add)
for y in range(n):
    print(add[y])
    out_file.write(add[y])