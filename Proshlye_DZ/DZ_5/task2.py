"""
2) Создать текстовый файл (не программно), сохранить в нем
несколько строк, выполнить подсчет количества строк, количества слов в
каждой строке.
"""

f = open('texsts/tests_2.txt')
line = 0
for i in f:
    line += 1

    flag = 0
    word = 0
    for j in i:
        if j != ' ' and flag == 0:
            word += 1
            flag = 1
        elif j == ' ':
            flag = 0

    print(i, len(i), 'символ /-ов,', word, 'слов,')

print(line, 'строк,')
f.close()
