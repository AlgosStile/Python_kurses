"""
Даны два файла, в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов.*
Пример:

            - 2*x² + 4*x + 5 = 0
            - 5*x² + 2*x + 43 = 0
            - Результат: 7*x^2 + 6*x + 48 = 0
*Значения коэффициентов от -100 до 100
*Сумма многочленов с разными степенями
Пример:
- 2*x² + 4*x + 5 = 0
- 5*x^4 + 2*x^3 - 6*x^2 + 13*x + 43 = 0
- Результат: 5*x^4 + 2*x^3 - 4*x^2 + 17*x + 48 = 0
"""

with open('log_s_1.txt', 'r') as file:
    m_1_m = file.read()
    m_1_m = m_1_m[0:-4]

with open('log_s_2.txt', 'r') as file:
    m_2_m = file.read()

with open('log_s_3.txt', 'w', encoding='utf-8') as file:
    file.write(f'{m_1_m} + {m_2_m}')