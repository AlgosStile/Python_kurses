"""
Задача: предложить улучшения кода для уже решённых задач(3-5 задач):
С помощью использования лямбд, filter, map, zip, enumerate,
list comprehension
"""

# Было так:

# float_num = input('Введите число: ')
#
# sum_1: int = 0
# for i in float_num:
#     if i != '.':
#         sum_1 += int(i)
# print(sum_1)


# Стало так:

n = input('Введите вещественное число: ')
sum_s = sum(map(int, n.replace('.', '')))
print(sum_s)
