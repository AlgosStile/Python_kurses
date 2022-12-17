"""
1) Создать программно файл в текстовом формате, записать в него
построчно данные, вводимые пользователем. Об окончании ввода данных
свидетельствует пустая строка.
"""
from datetime import time

my_func = open('texsts/tests.txt', 'w')
line = input('Введите текст: \n')
while line:
    my_func.writelines(line)
    line = input('Введите текст: \n')
    if not line:
        break

my_func.close()
my_f = open('texsts/tests.txt', 'r')
content = my_f.readlines()
print(content)
my_f.close()
