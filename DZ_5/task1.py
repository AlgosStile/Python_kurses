"""
Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
"""

my_text_s = 'Напишите абв напиабв програбвмму программу, удаляющую из \
    этого абв текста все вабвс слова, содерабващие содержащие "абв"'


def del_some_words(my_text: object) -> object:
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)


my_text_s = del_some_words(my_text_s)
print(my_text_s)
