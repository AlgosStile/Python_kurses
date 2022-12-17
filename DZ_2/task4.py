"""
Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях. Позиции хранятся в файле
file.txt в одной строке одно число.
"""

import random

f = open("file.txt")

input_num = 10
# input_num = int(f.readline(1))
# input_num = int(input('Введите число: '))
list_1 = []

for i in range(input_num):
    list_1.append(random.randint(input_num * -1, input_num))

print(list_1)
result = 1

for line in f:
    print(list_1[int(line)], ' * ', end='')
    result = result * list_1[int(line)]

print('= ', result)
