"""
Напишите программу, которая принимает на вход вещественное число и показывает
сумму его цифр.

    *Пример:*

    - 6782 -> 23
    - 0.56 -> 11
"""

float_num = input('input float number: ')

sum_1: int = 0
for i in float_num:
    if i != '.':
        sum_1 += int(i)
print(sum_1)
