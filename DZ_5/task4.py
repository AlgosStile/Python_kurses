"""
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

Входные и выходные данные хранятся в отдельных текстовых файлах.
"""

with open('encode.txt', 'w') as data:
    data.write(
        'ZZZZZZZZZZBBBZZZZZZZZZZBBBZZZZZZZZZZZZZZZZZBBBZZZZZZZZZZZZZZBBBZZZZ')

with open('file_1.txt', 'r') as data:
    string = data.readline()


def rle_encode(decoded_string_1):
    encoded_string_1 = ''
    count = 1
    char = decoded_string_1[0]
    for i in range(1, len(decoded_string_1)):
        if decoded_string_1[i] == char:
            count += 1
        else:
            encoded_string_1 = encoded_string_1 + str(count) + char
            char = decoded_string_1[i]
            count = 1
            encoded_string_1 = encoded_string_1 + str(count) + char
    return encoded_string_1


def rle_decode(encoded_string_1):
    decoded_string_1 = ''
    char_amount = ''
    for i in range(len(encoded_string_1)):
        if encoded_string_1[i].isdigit():
            char_amount += encoded_string_1[i]
        else:
            decoded_string_1 += encoded_string_1[i] * int(char_amount)
        char_amount = ''
    print(decoded_string_1)

    return decoded_string_1


with open('encode.txt', 'r') as file:
    decoded_string = file.read()

with open('file_decode.txt', 'w') as file:
    encoded_string = rle_encode(decoded_string)
    file.write(encoded_string)

print('Decoded string: \t' + decoded_string)
print('Encoded string: \t' + rle_encode(decoded_string))
print(
    f'Compress ratio: \t{round(len(decoded_string) / len(encoded_string), 1)}')
