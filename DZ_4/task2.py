"""
Задайте натуральное число N. Напишите программу, которая составит список
простых множителей числа N. (Выполнили на семинаре)
"""

n = int(input('Введите число -> '))
lst = [n]


def x(lst_1):
    fl = 0
    for i in range(lst_1[-1] // 2, 1, -1):
        if lst_1[len(lst_1) - 1] % i == 0:
            lst_1.append(i)
            lst_1[-2] = lst_1[-2] // i
            fl += 1

    if fl != 0:
        x(lst_1)


x(lst)

print(lst)