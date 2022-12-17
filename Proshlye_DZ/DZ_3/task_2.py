"""
2) Реализовать функцию, принимающую несколько параметров, описывающих
данные пользователя: имя, фамилия, год рождения, город проживания, email,
телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def personal_data(name: object, lastname: object, year_of_birth: object,
                  city: object, email: object, phone: object) -> object:
    """

    :rtype: object
    """
    return print(
        f'Имя: {name} Фамилия: {lastname} Год рождения: {year_of_birth}'
        f'Город проживания: {city} Email: {email} Телефон: {phone}')


personal_data(
    name=input('Имя: '),
    year_of_birth=input('Год Рождения: '),
    lastname=input('Фамилия: '),
    city=input('Город проживания: '),
    email=input('email: '),
    phone=input('phone: '),
)
