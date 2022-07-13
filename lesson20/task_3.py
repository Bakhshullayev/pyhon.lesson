""" Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing """
import random


def method1(x, y, z):
    return max(x, y, z)


def method2(x, y, z):
    if x > y:
        if x > z:
            return x
    if y > x:
        if y > z:
            return y
    if z > x:
        if z > y:
            return z


def method3(x, y, z):
    max_ = x

    if x > max_:
        max_ = x
    if y > max_:
        max_ = y
    if z > max_:
        max_ = z

    return max_


def method4(temp):
    max_ = temp[0]

    for son in temp:
        if son > max_:
            max_ = son

    return max_


temp = []
for i in range(100):
    temp.append(random.randint(0, 1000))

print(method4(temp))
