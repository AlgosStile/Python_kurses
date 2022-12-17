"""
3) Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(arg1: object, arg2: object, arg3: object) -> object:
    print(
        f'Сумма двух наибольших аргументов равна: \n'
        f' {arg1 + arg2 + arg3 - min([arg1, arg2, arg3])}')


my_func(
    int(input('Аргумент 1:')),
    int(input('Аргумент 2:')),
    int(input('Аргумент 3:')),
)
