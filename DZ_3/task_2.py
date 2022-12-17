"""
Задайте список из вещественных чисел. Напишите программу,
которая найдёт разницу между максимальным и минимальным значением дробной
части элементов.

    *Пример:*

    - [1.1, 1.2, 3.1, 5.1, 10.01] => 0.19
"""

n = [1.1, 1.2, 3.1, 10.01]


def average(n):
    max_1 = 0
    min_1 = 1  #
    for i in n:
        temp = round(i % 1, 3)  #
        if temp > max_1:
            max_1 = temp
        elif temp < min_1:
            min_1 = temp
    print(f"max {max_1} min {min_1}")
    res = max_1 - min_1
    return res


print(average(n))
