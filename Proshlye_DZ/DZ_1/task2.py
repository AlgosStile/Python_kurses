# 2) Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time_sec = int(input('Введите число: '))
hours: int = time_sec // 3600
hours_res = ('0' + str(hours)) if hours <= 10 else (hours)
minutes: int = (time_sec % 3600) // 60
minutes_res = ('0' + str(minutes)) if minutes <= 10 else (minutes)
seconds: int = (time_sec % 3600) % 60
seconds_res = ('0' + str(seconds)) if seconds <= 10 else (seconds)
if hours > 24:
    print(
        'Количество часов превышает допустимое, скорректируйте ввод заново')
else:
    print(f'Msk: {hours_res}:{minutes_res}:{seconds_res}')
