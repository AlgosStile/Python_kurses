"""
Задача: предложить улучшения кода для уже решённых задач(3-5 задач):
С помощью использования лямбд, filter, map, zip, enumerate,
list comprehension
"""

# Было так:

# import math
#
# ax = float(input('Введите координаты точки a по оси x:'))
# ay = float(input('Введите координаты точки a по оси y:'))
# bx = float(input('Введите координаты точки b по оси x:'))
# by = float(input('Введите координаты точки b по оси y:'))
#
# dist = math.sqrt((ax - bx) ** 2 + (ay - by) ** 2)
# print(f'Расcтояние между точкой A до точки B = {dist}')

#Стало так:

from functools import reduce

dot_1 = list(map(int, input(
    'Введите две координаты первой точки A, через пробел: ').split()))
dot_2 = list(map(int, input(
    'Введите две координаты второй точки B, через пробел: ').split()))


def dot_range(dot_s, dot_t):
    rng = reduce(lambda x, y: (x + y) ** (1 / 2),
                 (map(lambda dot: (dot[1] - dot[0]) ** 2, zip(dot_s, dot_t))))
    return round(rng, 2)


print(dot_range(dot_1, dot_2))
