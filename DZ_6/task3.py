"""
Задача: предложить улучшения кода для уже решённых задач(3-5 задач):
С помощью использования лямбд, filter, map, zip, enumerate,
list comprehension
"""

# Было так:
# def multiply_sp(sp_1):
#     if len(sp_1) % 2 != 0:
#         print("Количество элементов списка не четное!")
#         rz = int(len(sp_1) / 2) + 1
#     else:
#         rz = int(len(sp_1) / 2)
#
#     mult = []
#     for i in range(0, rz):
#         mult.append(sp_1[i] * sp_1[len(sp_1) - 1 - i])
#     return mult
#
#
# if __name__ == "__main__":
#     #    sp = [2, 3, 4, 5, 6]
#     sp = [2, 3, 5, 6]
#     print(sp, " => ", multiply_sp(sp))


# Стало:
import math

list_a = list(map(int, input('Введите числа, через пробел: ').split()))
print('Исходный список: ', list_a)
print('Результат: ', list([a * b for a, b in
                           zip(list_a[0:math.ceil(len(list_a) / 2)],
                               list_a[::-1])]))
