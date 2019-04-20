# -*- coding: utf-8 -*-

def my_abs(x):
    if x >=0:
        return x
    else:
        return -x

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print (my_abs(-99))

print (add_end())

print (calc(1, 2, 3))