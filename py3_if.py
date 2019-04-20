#!/usr/bin/env python3
# -*- coding: utf-8 -*-

age = 20
if age >=20:
    print('your age is', age)
    print('adult')

age = 30
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')

s = input('birth: ')
birth = int(s)
if birth <2000:
    print('00前')
else:
    print('00后')