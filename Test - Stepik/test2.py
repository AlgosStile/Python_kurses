"""
Сумма делителей
На вход программе подается натуральное число nn. Напишите программу, \
которая вычисляет сумму всех его делителей.
Входные данные
На вход программе подается натуральное число n.
Выходные данные
Программа должна вывести единственное число в соответствии с условием задачи.
"""
# n = int(input())
# counter = 0
# for i in range(1, n + 1):
#     if n % i == 0: # находим делитель, если остаток от деления равен нулю
#         counter += i  # прибавляем к переменной текущий делитель
# print(counter)

# ++++++++++++++++++++++++++++++++
"""
Знакочередующаяся сумма
На вход программе подается натуральное число nn. Напишите программу вычисления 
знакочередующей суммы 
1−2+3−4+5−6+…+(−1)**n+1 * n.
"""
# n = int(input())
# res = 0
# for i in range(1, n + 1):  # цикл от 1 до числа n
#     if i % 2 == 0:
#         res -= i  # если i делиться без остатка, то вычитает из предыдущего
#         # результата
#     if i % 2 != 0:
#         res += i  # если i делиться с остатком, то прибавляем к предыдущему
#         # результату
# print(res)

# ++++++++++++++++++++++++++++++++
"""
Наибольшие числа 🌶️🌶️
На вход программе подается натуральное число nn, а затем nn различных 
натуральных чисел, каждое на отдельной строке. Напишите программу, которая 
выводит наибольшее и второе наибольшее число последовательности.
Формат входных данных
На вход программе подаются натуральное число n >= 2, а затем n различных 
натуральных чисел, каждое на отдельной строке.
"""
# n = int(input())
# max1 = max2 = 1  # пусть самое большое число это минимально возможное
# for i in range(1, n + 1):  # цикл от 1 до n
#     a = int(input())  # получаем вводимое число
#     if a > max1:  # если введенное число больше нашего максимума, то это новый максимум
#         max2 = max1  # запоминаем предыдущее наибольшее число в переменной max2
#         max1 = a  # а само это число на входе становится наибольшим
#     elif a > max2:  # если число не больше max1, то проверяем больше ли оно второго max2
#         max2 = a
# print(max1)
# print(max2)

# ++++++++++++++++++++++++++++++++
"""
Only even numbers 🌶️
Напишите программу, которая считывает последовательность из 10 целых чисел 
и определяет является ли каждое из них четным или нет.

Формат входных данных
На вход программе подаются 10 целых чисел, каждое на отдельной строке.
"""

# flag = 'YES'         # по умолчанию считаем что последовательность четная
# for _ in range(10):  # цикл до 10
#     a = int(input()) # получаем число
#     if a % 2 != 0:   # проверяем делимость числа на остаток
#         flag = 'NO'  # если число имеет остаток то NO
# print(flag)

# ++++++++++++++++++++++++++++++++
"""
Последовательность Фибоначчи.
Напишите программу, которая считывает натуральное число n и выводит первые n 
чисел последовательности Фибоначчи.
Формат входных данных
На вход программе подается одно число n (n≤100) – количество членов 
последовательности.
Формат выходных данных
Программа должна вывести члены последовательности Фибоначчи, 
отделенные символом пробела.
"""
# n = int(input())  # вводим число и получаем кол-во циклов
# num1 = 0  # число 1
# num2 = 1  # число 2
# for i in range(n):  # цикл до "n"
#     num2 = num1 + num2  # присваиваем переменной num2 новое значение суммы
#     этой переменной с предыдущей
#     num1 = num2 - num1  # переменной num1 присваиваем значение которое было
#     в num2
#     print(num1, end=' ')

# ++++++++++++++++++++++++++++++++
"""
До КОНЦА 1
На вход программе подается последовательность слов, каждое слово на отдельной
строке. Концом последовательности является слово «КОНЕЦ» (без кавычек). 
Напишите программу, которая выводит члены данной последовательности.
"""

# text = input()
# while text != "КОНЕЦ":
#     print(text)
#     text = input()

# ++++++++++++++++++++++++++++++++
"""
До КОНЦА 2
На вход программе подается последовательность слов, каждое слово на 
отдельной строке. Концом последовательности является слово «КОНЕЦ» 
или «конец» (большими или маленькими буквами, без кавычек). 
Напишите программу, которая выводит члены данной последовательности.
"""
# text = input()
# while text != "КОНЕЦ" and text != "конец":
#     print(text)
#     text = input()

# ++++++++++++++++++++++++++++++++
"""
Количество членов
На вход программе подается последовательность слов, каждое слово на отдельной
строке. Концом последовательности является одно из трех слов:
«стоп», «хватит», «достаточно» (маленькими буквами, без кавычек). 
Напишите программу, которая выводит общее количество членов 
данной последовательности.
"""

# text = input()
# count = 0
# while text != "стоп" and text != "хватит" and text != "достаточно":
#     text = input()
#     count += 1
# print(count)

# ++++++++++++++++++++++++++++++++
"""
Пока делимся
На вход программе подается последовательность целых чисел делящихся на 77, 
каждое число на отдельной строке. Концом последовательности является любое 
число не делящееся на 77. Напишите программу, которая выводит члены данной 
последовательности.
"""
# num = int(input())
# count = 0
# while num % 7 == 0:
#     print(num)
#     num = int(input())
#     count += num

# ++++++++++++++++++++++++++++++++
"""
Сумма чисел
На вход программе подается последовательность целых чисел, каждое число 
на отдельной строке. Концом последовательности является любое отрицательное 
число. Напишите программу, которая выводит сумму всех членов данной 
последовательности.
"""
# num = int(input())
# count = 0
# while num >= 0:
#     count += num
#     num = int(input())
# print(count)

# ++++++++++++++++++++++++++++++++
"""
Количество пятерок
На вход программе подается последовательность целых чисел от 11 до 55, 
характеризующее оценку ученика, каждое число на отдельной строке. 
Концом последовательности является любое отрицательное число, либо число 
большее 5. Напишите программу, которая выводит количество пятерок.
Формат входных данных
На вход программе подается последовательность чисел, 
каждое число на отдельной строке.
Формат выходных данных
Программа должна вывести количество пятерок.
"""
# num = int(input())
# count = 0  # переменная для подсчета ко-ва пятерок
# while 1 <= num <= 5:  # выполняем цикл пока число в диапозоне от 1 до 5
#     if num == 5:  # проверяем пятерка это число или нет
#         count += 1  # если пятерка, то подсчитываем
#     num = int(input())  # получаем следующее введеное число
# print(count)

# ++++++++++++++++++++++++++++++++
"""
Ведьмаку заплатите чеканной монетой
Всем известно, что ведьмак способен одолеть любых чудовищ, однако его услуги
обойдутся недешево, к тому же ведьмак не принимает купюры, он принимает только
чеканные монеты. В мире ведьмака существуют монеты с номиналами 
1, 5, 10, 25.
Напишите программу, которая определяет какое минимальное количество чеканных 
монет нужно заплатить ведьмаку.
Формат входных данных 
На вход программе подается одно натуральное число, цена за услугу ведьмака.
"""

# price = int(input())  # получаем цену услуги ведьмака
# count = 0  # переменная для хранения кол-ва монет
#
# while price > 0:  # пока цена больше 0 выполняем цикл
#     if price >= 25:  # если цена больше или равен 25
#         price -= 25  # вычитаем из нее 25
#     elif price >= 10:  # иначе проверяем остаток больше или равен 10
#         price -= 10  # если да отнимаем 10
#     elif price >= 5:  # если остаток больше или равен 5
#         price -= 5  # то вычитаем 5
#     else:  # иначе остается менее 5 и вычитаем по монетке
#         price -= 1  # вычетаем по монетке
#     count += 1  # считаем кол-во монет, за один цикл вычитаем только 1
#     # номинал монеты в зависимости от условий
#
# print(count)

# ++++++++++++++++++++++++++++++++
"""
Обратный порядок 1
Дано натуральное число. Напишите программу, которая выводит его цифры 
в столбик в обратном порядке.
Формат входных данных 
На вход программе подается одно натуральное число
Формат выходных данных
Программа должна вывести цифры введенного числа в столбик в обратном порядке.
"""
# num = int(input())
# while num != 0: # пока в числе есть цифры
#     last_digit = num % 10 # получить последнюю цифру
#     num = num // 10 # удалить последнюю цифру из числа
#     print(last_digit)
# ++++++++++++++++++++++++++++++++
"""
Обратный порядок 2
Дано натуральное число. Напишите программу, которая меняет порядок цифр 
числа на обратный.
Формат входных данных 
На вход программе подается одно натуральное число.
Формат выходных данных
Программа должна вывести число, записанное в обратном порядке.
"""
# num = int(input())
# while num != 0:  # пока в числе есть цифры
#     last_digit = num % 10  # получить последнюю цифру
#     num = num // 10  # удалить последнюю цифру из числа
#     print(last_digit, end="")

# ++++++++++++++++++++++++++++++++
"""
max и min
Дано натуральное число n, \, (n \ge 10)n,(n≥10). Напишите программу, которая
определяет его максимальную и минимальную цифры.
Формат входных данных
На вход программе подается одно натуральное число.
Формат выходных данных
Программа должна вывести максимальную и минимальную цифры введенного числа
(с поясняющей надписью).
"""
# n = int(input())
# n = str(n)
# print("Максимальная цифра равна", max(n))
# print("Минимальная цифра равна", min(n))

# ++++++++++++++++++++++++++++++++
"""
Все вместе
Дано натуральное число. Напишите программу, которая вычисляет:
сумму его цифр;
количество цифр в нем;
произведение его цифр;
среднее арифметическое его цифр;
его первую цифру;
сумму его первой и последней цифры.
Формат входных данных 
На вход программе подается одно натуральное число.
"""
# num = int(input())
# n = num  # это наше число, неизменное
# total = 0  # сумма чисел
# product = 1  # произведение чисел
# count = 0  # количество чисел
#
# while num != 0:  # цикл пока num не равен 0
#     total += num % 10  # считаем суму чисел
#     product *= num % 10  # считаем произведение чисел
#     count += 1  # считаем количество чисел
#     num //= 10  # откидывает последнее число
#
# print(total)  # сумма чисел
# print(count)  # количество чисел
# print(product)  # произведение чисел
# print(total / count)  # среднее арифмитическое всех чисел
# print(n // 10 ** (count - 1))  # первое число
# print(
#     n // 10 ** (count - 1) + n % 10)  # произведение первого и последнего
#     чисел
# ++++++++++++++++++++++++++++++++
"""
Вторая цифра
Дано натуральное число n, (n > 9). Напишите программу, которая 
определяет его вторую (с начала) цифру.
Формат входных данных 
На вход программе подается одно натуральное число, состоящее как минимум 
из двух цифр.
Формат выходных данных
Программа должна вывести его вторую (с начала) цифру.
"""
# n = int(input())
# second_digit = 0  # назначаем переменную для дальнейшего использования
# while n > 9:
#     second_digit = n % 10  # находим последнию цифру
#     n = n // 10  # убираем последнюю цифру
# print(second_digit)

# ++++++++++++++++++++++++++++++++
"""
Одинаковые цифры
Дано натуральное число. Напишите программу, которая определяет, состоит ли 
указанное число из одинаковых цифр.
Формат входных данных 
На вход программе подается одно натуральное число.
Формат выходных данных
Программа должна вывести «YES» если число состоит из одинаковых цифр и «NO» 
в противном случае.
"""
# num = int(input())  # ввод числа
# flag = True  # флаг считаем что все цифры равны
#
# while num > 9:  # пока число 2-х значное выполняем цикл
#     last = num % 10  # вычисляем последнюю цифру
#     num = num // 10  # удаляем последнюю цифру и запускаем цикл сначала
#     sec = num % 10  # вычисляем предпоследнюю цифру
#     if last != sec:  # условие, если последняя и предпоследняя не равны
#         flag = False  # и если цифры не равны, меняем флаг
#
# if flag:  # если флаг true(верно)
#     print('YES')  # значит цифры равны
# else:
#     print('NO')  # иначе различны
# ++++++++++++++++++++++++++++++++

"""
Упорядоченные цифры 🌶️
Дано натуральное число. Напишите программу, которая определяет, 
является ли последовательность его цифр при просмотре справа налево 
упорядоченной по неубыванию.
Формат входных данных 
На вход программе подается одно натуральное число.
Формат выходных данных
Программа должна вывести «YES» если последовательность его цифр при 
просмотре справа налево является упорядоченной по неубыванию и «NO» 
в противном случае.
"""
# num = int(input())
# flag = 'YES'  # используем флаг и считаем что последовательность упорядочена
# a = num % 10  # находим послееднюю цифру числа
#
# while num:  # запускаем цикл
#     if a > num % 10:  # условие если предыдущая цифра больше последующей
#         flag = 'NO'  # то присваиваем флаг NO, и уже нет смысла записывать в "a" последнию цифру
#     else:  # иначе
#         a = num % 10  # присваиваем последнюю цифру - переменной
#     num //= 10  # удаляем последнюю цифру числа
# print(flag)

# ++++++++++++++++++++++++++++++++
"""
Наименьший делитель
На вход программе подается число n > 1. Напишите программу, которая выводит 
его наименьший отличный от 1 делитель.
Формат входных данных
На вход программе подается одно натуральное число n.
Формат выходных данных
Программа должна вывести наименьший делитель отличный от 1.
Примечание. Используйте оператор break при обнаружении делителя.
"""
# n = int(input())
# for i in range(2, n + 1):  # начинаем делить с 2
#     if n % i == 0:  # поиск минимального делителя
#         break  # прерываем если нашли делитель
# print(i)

# ++++++++++++++++++++++++++++++++
"""
Следуй правилам
На вход программе подается натуральное число n. Напишите программу, 
которая выводит числа от 1 до n включительно за исключением:
чисел от 5 до 9 включительно;
чисел от 17 до 37 включительно;
чисел от 78 до 87 включительно.
Формат входных данных
На вход программе подается одно натуральное число n.
"""
# n = int(input())
# for i in range(1, n + 1):
#     if 5 <= i <= 9:
#         continue
#     if 17 <= i <= 37:
#         continue
#     if 78 <= i <= 87:
#         continue
#     print(i)
# ++++++++++++++++++++++++++++++++
"""
Ревью кода-1 🌶️🌶️
На обработку поступает последовательность из 10 целых чисел. Известно, 
что вводимые числа по абсолютной величине не превышают 10**6.
Нужно написать программу, которая выводит на экран количество 
неотрицательных чисел последовательности и их произведение. 
Если неотрицательных чисел нет, требуется вывести на экран «NO». 
Программист торопился и написал программу неправильно.
Найдите все ошибки в этой программе (их ровно 4). Известно, 
что каждая ошибка затрагивает только одну строку и может быть исправлена 
без изменения других строк.
Вот сам код:
count = 0
p = 0
for i in range(1, 10):
    x = int(input())
    if x > 0:
        p = p * x
        count = count + 1
if count > 0:
    print(x)
    print(p)
else:
    print('NO')
"""
# count = 0
# p = 1  # ошибка: p не должно быть равно 0
# for i in range(1, 11):  # ошибка: range(1, 10) это 9 итераций - 9 цифр
#     x = int(input())
#     if x > -1:  # ошибка: х тоже не отрицательное число
#         p = p * x
#         count = count + 1
# if count > 0:
#     print(count)  # ошибка: печатаем счетчик, а не переменную
#     print(p)
# else:
#     print('NO')

# ++++++++++++++++++++++++++++++++
"""
Ревью кода-2 🌶️🌶️
На обработку поступает последовательность из 1010 целых чисел. Известно, 
что вводимые числа по абсолютной величине не превышают 10**6.
Нужно написать программу, которая выводит на экран сумму всех 
отрицательных чисел последовательности и максимальное отрицательное число
в последовательности. Если отрицательных чисел нет, требуется вывести на
экран «NO». Программист торопился и написал программу неправильно.
Найдите все ошибки в этой программе (их ровно 5). Известно, 
что каждая ошибка затрагивает только одну строку и может быть исправлена
без изменения других строк.
Вот сам код:
mx = 0
s = 0
for i in range(11):
    x = int(input())
    if x < 0:
        s = x
    if x > mx:
        mx = x
print(s)
print(mx)
"""
# mx = - pow(10, 6)  # изменение стартового значения мах на минимально возможное
# s = 0
# for i in range(1, 11):  # появилось начало последовательности
#     x = int(input())
#     if x < 0:
#         s += x  # добавился +, чтобы считать сумму
#     if 0 > x > mx:
#         mx = x
# if s < 0:  # добавление оператора условия
#     print(s)
#     print(mx)
# else:  # добавление второго варианта ответа
#     print('NO')

# ++++++++++++++++++++++++++++++++
"""
Ревью кода-3
На обработку поступает последовательность из 7 целых чисел. Известно, 
что вводимые числа по абсолютной величине не превышают 10**6.
Нужно написать программу, которая подсчитывает и выводит сумму всех чётных 
чисел последовательности или 0, если чётных чисел в последовательности нет.
Программист торопился и написал программу неправильно.
Найдите все ошибки в этой программе (их ровно 4). Известно, что каждая 
ошибка затрагивает только одну строку и может быть исправлена без 
изменения других строк.
Примечание 1. Число x не превышает по абсолютной величине 10^6,
если -106 ≤ x ≤106
Примечание 2. При необходимости вы можете добавить необходимые строки кода.
s = 1
for i in range(1, 7):
    n = input()
    if i % 2 == 0:
        s = s + n
print(s)
"""
# s = 0  # неверно задана переменная (было 1)
# for i in range(7):  # неверно заданы границы диапазона (было (1, 7))
#     n = int(input())  # отсутствие преобразования в int число(не было int())
#     if n % 2 == 0:  # неправильная переменная в условии (была i а не n)
#         s = s + n
# print(s)

# ++++++++++++++++++++++++++++++++
"""
Ревью кода-4 ?️?️
На обработку поступает натуральное число. Нужно написать программу, 
которая выводит на экран максимальную цифру числа, кратную 3. 
Если в числе нет цифр, кратных 3, требуется на экран вывести «NO». 
Программист торопился и написал программу неправильно.
Найдите все ошибки в этой программе (их ровно 5). Известно, что каждая 
ошибка затрагивает только одну строку и может быть исправлена 
без изменения других строк.
Примечание 1. Число 0 делится на любое натуральное число.
Примечание 2. При необходимости вы можете добавить нужные строки кода.
n = int(input())
max_digit = n % 10
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit < max_digit:
            digit = max_digit
    n = n % 10
if max_digit == 0:
    print('NO')
else:
    print(max_digit)
"""
# n = int(input())
# max_digit = -1  # меняем значение на -1, чтобы любая цифра могла заменить его
# while n > 0:
#     digit = n % 10
#     if digit % 3 == 0:
#         if digit > max_digit:  # нужно найти большее число а не меньшее
#             max_digit = digit  # перепутал местами
#     n //= 10  # нужно откинуть последнюю цифру
# if max_digit == -1:  # сравнивать нужно не с 0, а с -1
#     print('NO')
# else:
#     print(max_digit)

# ++++++++++++++++++++++++++++++++
"""
Ревью кода-5 ?️
На обработку поступает натуральное число. 
Нужно написать программу, которая выводит на экран его
первую (старшую) цифру. Программист торопился и написал программу 
неправильно. Найдите все ошибки в этой программе (их ровно 2). 
Известно, что каждая ошибка затрагивает только одну строку и может 
быть исправлена без изменения других строк.
n = int(input())
while n > 0:
    n %= 10
print(n)
"""
# n = int(input())
# while n > 9:  # Ошибка - цикл имеет смысл только в случае числа больше 0
#     n //= 10  # Ошибка - используем знак // для получения 1 цифры а не %
# print(n)
# ++++++++++++++++++++++++++++++++
"""
Ревью кода-6
На обработку поступает натуральное число. Нужно написать программу,
которая выводит на экран произведение цифр введенного числа. 
Программист торопился и написал программу неправильно.
Найдите все ошибки в этой программе (их ровно 3). 
Известно, что каждая ошибка затрагивает только одну строку и может 
быть исправлена без изменения других строк.
n = input()
product = n % 10
while n >= 10:
    digit = n % 10
    product = product * digit
    n //= 10
print(product)
"""
# n = int(input())  # вводим число, а не текст
# product = 1  # число может быть любым, кроме 0, а было произведение чисел
# while n > 0:  # цикл должен начинаться с 0, иначе мы потеряем цикл
#     digit = n % 10
#     product *= digit
#     n //= 10
# print(product)

# ++++++++++++++++++++++++++++++++
"""
Таблица-1
Дано натуральное число n(n≤ 9). Напишите программу, которая печатает таблицу
размером n×3 состоящую из данного числа (числа отделены одним пробелом).
Формат входных данных
На вход программе подается одно натуральное число.
Формат выходных данных
Программа должна вывести таблицу размером n×3 состоящую из данного числа.
Примечание. В конце строки может быть пробел.
"""
# n = int(input())
# for _ in range(n):
#     for _ in range(2):  # чтобы не выводить лишний пробел в конце строки,
#         print(n, end=' ')  # во вложенном цикле выводим только два столбика,
#     print(n)  # а третий столбик выводим здесь, во внешнем цикле

# ++++++++++++++++++++++++++++++++
"""
Таблица-2
Дано натуральное число n (n≤ 9). Напишите программу, которая печатает 
таблицу размером nx5, где в i-ой строке указано число i 
(числа отделены одним пробелом).
Формат входных данных
На вход программе подается одно натуральное число.
Формат выходных данных
Программа должна вывести таблицу размером n ×5 в соответствии с условием.
Примечание. В конце строки может быть пробел.
"""

# n = int(input())
# for i in range(1, n+1): # диапазон от 1 до n включительно
#     for j in range(5): # повторяем 5 раз
#         print(i, end=' ') # печатаем i и пробел в end=
#     print()

# ++++++++++++++++++++++++++++++++
"""
Таблица-3
Дано натуральное число n(n≤ 9). Напишите программу, которая печатает 
таблицу сложения для всех чисел от 1 до n в соответствии с примером.
Формат входных данных
На вход программе подается одно натуральное число.
Формат выходных данных
Программа должна вывести таблицу сложения для всех чисел от 1 до n.
Примечание. В конце строки может быть пробел.
"""
# n = int(input())
# for i in range(1, n + 1):  # каждый нов. цикл буд. выводиться следующее число i
#     for j in range(1, 10):  # выводим последовательность от 1 до 9
#         print(i, '+', j, '=', j + i)  # выводим таблицу сложения
#     print()

# ++++++++++++++++++++++++++++++++
"""
Звездный треугольник 🌶️🌶️
Дано нечетное натуральное число n. Напишите программу, которая печатает 
равнобедренный звездный треугольник с основанием, равным n в соответствии 
с примером:
*
**
***
**
*
"""
# n = int(input())
# center = n // 2 + 1  # находим середину
# count = 0  # кол-во звезд в строке
# for i in range(1, n + 1):
#     if i > center:
#         count -= 1  # если перешли за середину то убавляем кол-во звезд
#     else:
#         count += 1  # иначе прибавляем кол-во звезд
#     for _ in range(count):  # выполняем цикл сколько нужно звезд
#         print('*', end='')
#     print()

# ++++++++++++++++++++++++++++++++
"""
Численный треугольник 1
Дано натуральное число n. Напишите программу, которая печатает 
численный треугольник в соответствии с примером:
1
22
333
4444
55555
…
Формат входных данных
На вход программе подается одно натуральное число.
"""
# n = int(input())
# for i in range(1, n+1):    # строки n
#     for j in range(i):     # столбцы
#         print(i, end='')
#     print()

# ++++++++++++++++++++++++++++++++
"""
Численный треугольник 3
Дано натуральное число n. 
Напишите программу, которая печатает численный 
треугольник с высотой равной nn, в соответствии с примером:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
…
Формат входных данных
На вход программе подается одно натуральное число.
Формат выходных данных
Программа должна вывести треугольник в соответствии с условием.
Примечание. Используйте вложенный цикл for.
"""
# num = int(input())  # Определение высоты массива
# count = 0  # Порядковый номер цифры = число в массиве
# for x in range(1, num + 1):  # Первый цикл высоты массива
#     for y in range(x):  # Второй цикл длины массива
#         count += 1  # увеличиваем счетчик
#         print(count, end=' ')  # Вывод текущего числа и в конце пробел
#     print()  # Переход к новой строке
# ++++++++++++++++++++++++++++++++
"""
Численный треугольник 4
Дано натуральное число n. Напишите программу, которая печатает численный 
треугольник с высотой равной nn, в соответствии с примером:
1
121
12321
1234321
123454321
…
Формат входных данных
На вход программе подается одно натуральное число.Формат выходных данных
Программа должна вывести треугольник в соответствии с условием.
Примечание. Используйте вложенный питон цикл for.
"""
# num = int(input())
#
# for i in range(1, num + 1):  # цикл отвечающий за количество рядов
#     count = 0  # счетчик для ряда, при новом цикле обнуляется
#     for j in range(i):  # 1й вложенный
#         count += 1  # увеличиваем цифру в ряду
#         print(count, end='')  # вывод на печать без пробелов
#     for k in range(i, 1, -1):  # 2й вложенный
#         count -= 1  # уменьшаем цифру в ряду
#         print(count, end='')  # вывод на печать без пробелов
#     print()  # переход на новую строку

# ++++++++++++++++++++++++++++++++
"""
Делители-1 ?️
На вход программе подается два натуральных числа a и b (a < b). 
Напишите программу, которая находит натуральное число из отрезка [a;b] 
с максимальной суммой делителей.
Формат входных данных
На вход программе подаются два числа, каждое на отдельной строке.
Формат выходных данных
Программа на python должна вывести два числа на одной строке, 
разделенных пробелом: число с максимальной суммой делителей и сумму 
его делителей.
Примечание. Если таких чисел несколько, то выведите наибольшее из них.
"""
# a, b = int(input()), int(input())
# total_maximum = 0  # сумма делителей
# digit = 0  # число с максимальной суммой делителей
#
# for i in range(a, b + 1):  # цикл перебирающий все числа от a до b включительно
#     maximum = 0  # обнуление суммы делителей, для нового цикла
#     for j in range(1, i + 1):  # проверяем все числа от 1 до числа не превышающего проверяемое
#         if i % j == 0:  # проверка на деление без остатка
#             maximum += j  # суммируем делители
#         if maximum >= total_maximum:  # если сумма делителей больше max суммы делителей
#             total_maximum = maximum  # записываем в переменную максимальную
#             digit = j
# print(digit, total_maximum)  # вывод
# ++++++++++++++++++++++++++++++++
"""
Делители-2
На вход программе подается натуральное число n. Напишите программу, 
выводящую графическое изображение делимости чисел от 1 до n включительно. 
В каждой строке надо напечатать очередное число и столько символов «+», 
сколько делителей у этого числа.
Формат входных данных
На вход программе подается одно натуральное число.
Формат выходных данных
Программа должна вывести графическое изображение чисел от 1 до n, 
каждое на отдельной строке.
"""
# n = int(input())
#
# for i in range(1, n + 1):  # циклом перебираем все числа от 1 до n включительно
#     print(i, end='')  # вывод текущего числа
#     for j in range(1, i + 1):  # цикл поиска делителя
#         if i % j == 0:  # если число делится без остатка
#             print('+', end='')  # то печатаем + без пробела
#     print()  # переход на новую строку
# ++++++++++++++++++++++++++++++++
"""
Цифровой корень
На вход программе подается натуральное число n. Напишите программу, 
которая находит цифровой корень данного числа. Цифровой корень числа 
n получается следующим образом: если сложить все цифры этого числа, 
затем все цифры найденной суммы и повторить этот процесс, то в результате 
будет получено однозначное число (цифра), которое и называется цифровым 
корнем данного числа.
Формат входных данных
На вход программе подается одно натуральное число.
Формат выходных данных
Программа должна вывести цифровой корень введенного числа.
Примечание. Используйте вложенные циклы while.
"""

# n = int(input())  # ввод числа
#
# while n > 9:  # до тех пор, пока в числе n не останется одна цифраа
#     s = 0
#     while (n > 0):
#         last_digit = n % 10  # получить последнюю цифру
#         s += last_digit  # к числу прибавляем последнюю цифру
#         n = n // 10  # удалить последнюю цифру из числа
#     n = s
#
# print(n)

# ++++++++++++++++++++++++++++++++
"""
Сумма факториалов
Дано натуральное число nn. Напишите программу, которая выводит значение 
суммы 1!+2!+3!+…+n!.
Формат входных данных
На вход программе подается одно натуральное число.
Формат выходных данных
Программа должна вывести значение суммы 1!+2!+3!+…+n!.
Примечание 1. Факториалом натурального числа nn, называется 
произведение всех натуральных чисел от 1 до n, то есть n!=1⋅2⋅3⋅…⋅n
Примечание 2. Задачу можно решить без вложенного цикла. 
Напишите две версии программы.
"""
# num = int(input())  # кол-во факториалов
# total = 0  # сумма факториалов
# factorial = 1  # вычисляемый факториал
#
# for i in range(1, num + 1):  # перебираем факториалы
#     for j in range(1, i + 1):  # вычисляем каждый факториал
#         factorial *= j  # вычисляем факториал
#     total += factorial  # Суммируем факториалы чисел.
#     factorial = 1  # "обнуляем факториал"
# print(total)
# ++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++
"""
Простые числа
На вход программе подается два натуральных числа a и b (a < b). 
Напишите программу, которая находит все простые числа от a до b включительно.
Формат входных данных
На вход программе подаются два числа, каждое на отдельной строке.
Формат выходных данных
Программа должна вывести все простые числа от aa до b включительно, 
каждое на отдельной строке.
Примечание. Число 1 простым не является.
"""
# a, b, = int(input()), int(input())
# for i in range(a, b + 1):
#     if i == 1:                # 1 не является простым числом
#         continue              # пропускаем цикл
#     for j in range(2, i):     # перебираем делители от 2 до i
#         if i % j == 0:        # если делится без остатка, то оно не простое
#             break             # завершаем вложенный цикл
#     else:
#         print(i)
# ++++++++++++++++++++++++++++++++
# b = 1729
# x = 0
# s = [b]
# while x != 33:
#     for x in range(1, 34):
#         for y in range(1, 34):
#             for z in range(1, 34):
#                 for t in range(1, 34):
#                     for r in range(1, 34):
#                         if (x ** 3 + y ** 3) == (z ** 3 + t ** 3):
#                             if x != y and x != z and x != t and y != z and y != t and z != t:
#                                 a = (x ** 3 + y ** 3)
# if a != b:
#     if a not in s:
#         s.append(a)
# s.sort()
# b = a
# print(s)

# ++++++++++++++++++++++++++++++++
"""
На вход программе подается одна строка. Напишите программу, которая выводит 
элементы строки с индексами 0, 2, 4, ... в столбик.
Формат входных данных
На вход программе подается одна строка.
Формат выходных данных
Программа должна вывести элементы строки с индексами 0, 2, 4, ..., каждое 
на отдельной строке.
"""

# s = input()
# for i in range(0, len(s), 2):
#     print(s[i])

# ++++++++++++++++++++++++++++++++
"""
В столбик 2
На вход программе подается одна строка. Напишите программу, 
которая выводит в столбик элементы строки в обратном порядке.
Формат входных данных
На вход программе подается одна строка.
Формат выходных данных
Программа должна вывести в столбик элементы строки в обратном порядке.
"""
# text = input()
# for i in range(1, len(text)+1):
#     print(text[-i])

# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++
