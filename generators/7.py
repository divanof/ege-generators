import os
from random import randint
from random import shuffle
from math import log, ceil


if not os.path.exists('../tasks'):
    os.mkdir('../tasks')
f = open('../tasks/7.txt', 'a')


def answer(var, *args):
    if var == 1:
        x, y, n, tp1 = args
        if tp1:
            return x * y * ceil(log(n, 2)) / 2 ** 23
        return x * y * ceil(log(n, 2)) / 2 ** 23

    if var == 2:
        x, y, n, tp1 = args
        if tp1:
            return 2 ** int(n * 2 ** 23 / x / y)
        return 2 ** int(n * 2 ** 13 / x / y)


"""
Какой минимальный объём памяти (в Кбайт) нужно зарезервировать, чтобы можно было сохранить любое растровое изображение размером 512 на 256 пикселей при условии, что в изображении могут использоваться 32 различных цвета? В ответе запишите только целое число, единицу измерения писать не нужно.
"""

for i in range(10):
    var = 2
    if var == 1:
        tp1 = randint(0, 1)
        # Даём данные в Кб или в Мб

        if randint(0, 1):
            x, y, n = 2 ** (randint(6, 11)), 2 ** (randint(7, 11)), randint(4, 2000)
            # типа сложнее
        else:
            x, y, n = 2 ** (randint(6, 11)), 2 ** (randint(7, 11)), 2 ** randint(4, 10)
            # типа проще

        text = f"Какой минимальный объём памяти (в Кбайт) нужно зарезервировать, чтобы можно было сохранить любое растровое изображение размером { x } на { y } пикселей при условии, что в изображении могут использоваться { n } различных цвета? В ответе запишите только целое число, единицу измерения писать не нужно.\n"
        ans = answer(var, x, y, n, tp1)
        text += f"Ответ: { ans }\n"
        if tp1:
            text = text.replace('Кбайт', 'Мбайт')
        if ans:
            f.write(text)

    if var == 2:
        tp1 = randint(0, 1)
        # Даём данные в Кб или в Мб

        x, y, n = 2 ** (randint(6, 9)), 2 ** (randint(7, 9)), 2 ** randint(4, 5)
        if tp1:
            n //= 2 ** 4
            x *= 2 ** 3
            y *= 2 ** 3
        print(x, y, n)
        text = f"Рисунок размером { x } на { y } пикселей занимает в памяти { n } Кбайт (без учёта сжатия). Найдите максимально возможное количество цветов в палитре изображения.\n"
        ans = answer(var, x, y, n, tp1)
        text += f"Ответ: { ans }\n"
        if tp1:
            text = text.replace('Кбайт', 'Мбайт')
        if ans and ans != 1:
            f.write(text)
