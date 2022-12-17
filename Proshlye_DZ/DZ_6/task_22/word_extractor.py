# imports
from memory_profiler import profile
import requests


class BaseExtractor:
    # декоратор, который указывает, какую функцию отслеживать
    @profile
    def parse_list(self, array):
        # создаем файловый объект
        f = open('words.txt', 'w')
        for word in array:
            # запись слов в файл
            f.writelines(word)

    # декоратор, который указывает, какую функцию отслеживать
    @profile
    def parse_url(self, url):
        # получаем ответ
        response = requests.get(url).text
        with open('url.txt', 'w') as f:
            # Написание ответа в файл
            f.writelines(response)

"""
В написании кода используется профилировщик памяти
благодаря чему можно отследить, замерить, сколько было затрачено
оперативной памяти на выполнение кода
С помощью команды "pip install memory-profiler requests" введенной в
терминал я установил memory-profiler.
После того как основной код написан, я напишу код драйвера,
который будет вызывать функции этого класса
Продолжение в файле run.py (текущей директории)
"""
