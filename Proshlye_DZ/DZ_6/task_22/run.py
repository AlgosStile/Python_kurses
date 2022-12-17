from word_extractor import BaseExtractor

if __name__ == "__main__":
    # url for word list (huge)
    url = \
        'https://raw.githubusercontent.com/dwyl/english-words/master/words.txt'

    array = ['one', 'two', 'three', 'four', 'five']

    extractor = BaseExtractor()

    extractor.parse_url(url)

    extractor.parse_list(array)

"""
После глубокого анализа я сделал вывод, что parse_url() будет потреблять
больше памяти, чем parse_list(), что очевидно, потому что parse_url 
вызывает URL-адрес и записывает содержимое ответа в текстовый файл, что требует 
больше времени на выполнение, оптимизировать это можно при помощи parse_list()
Если вы откроете ссылку, то обнаружите, что список слов огромен, а значит 
и памяти для чтения этого списка будет выделяться гораздо больше, чем в случае
с кодом parse_list().
Теперь, чтобы протестировать это код, нужно запустите скрипт "run.py"
и мы увидим, что parse_url выполняется с выделением памяти Increment: 0.7 MiB
а parse_list() с Increment: 0.0 MiB что и является отличным результатом!
"""
