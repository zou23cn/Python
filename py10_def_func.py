#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


def move(x, y, step, angle=0):
    nx = x + step + math.cos(angle)
    ny = y + step + math.sin(angle)
    return nx, ny


n = my_abs(-20)
print(n)

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)


def nop():
    pass


def power1(x, ):
    return x * x


print(power1(5))
print(power1(15))


def power2(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power2(5,3))
