"""
Реализуйте алгоритм генерации случайного числа.(Не используя библиотеки
связанные с рандомом) (Доп задача, не влияющая на оценку)
"""

import random

lenght_1 = 20
list_1 = [i for i in range(lenght_1)]

print(list_1, '<-- not mixed')

for i in range(len(list_1)):
    r = random.randint(i, lenght_1 - 1)
    m = list_1[i]
    list_1[i] = list_1[r]
    list_1[r] = m

print(list_1, '<-- mixed')

random.shuffle(list_1)
print(list_1, '<-- shuffle')
