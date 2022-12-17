"""
Задача: написать функцию, принимающую одно целочисленное значение и
возвращающую сумму целых чисел от 0 до этого значения включительно.
При использовании нецелочисленного значения функция должна возвращать 0.
Вариант решения № 2
"""


def add(num):
    return sum(range(num + 1)) if type(num) == int else 0

"""
В этом примере кода который 
одновременно и максимально компактный, и легко читаемый, можно отметить 
отличную производительность и минимальное время на его выполнение, 
за счет короткого написания в 1 строку Время запуска составило 
2.6400084607303143e-05, при этом код в файле code_3 запускается еще быстрее
и требует меньше времени на его выполнение.
"""