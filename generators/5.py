import os
from random import randint
from random import shuffle


if not os.path.exists('../tasks'):
    os.mkdir('../tasks')
f = open('../tasks/5.txt', 'a')


def convert(n, bt):
    alpha = '0123456789ABCDEF'
    r = ''
    while n:
        r += alpha[n % bt]
        n //= bt
    return r[::-1]


def answer(res, cur, cur_sort, var):
    if var == 1:
        res = str(res)
        tmp = {
            'первая': 0,
            'вторая': 1,
            'третья': 2,
            'четвёртая': 3
        }

        for num in range(1000, 9999):
            num = str(num)
            n1 = int(num[tmp[cur[0]]]) + int(num[tmp[cur[1]]])
            n2 = int(num[tmp[cur[2]]]) + int(num[tmp[cur[3]]])
            if cur_sort == 'убывания':
                if res == (str(max(n1, n2)) + str(min(n1, n2))):
                    return num
            else:
                if res == (str(min(n1, n2)) + str(max(n1, n2))):
                    return num

    if var == 2:
        bases = {
            'двоичной': 2,
            'восьмиричной': 8,
            'десятичной': 10,
            'шестнадцатиричной': 16
        }
        base = bases[cur_sort]

        tp10 = lambda num: num + str(num.count('1') % 2)
        tp11 = lambda num: num + str(1 if (num.count('1') % 2) else 0)

        for num in range(1, 10000):
            k = bin(num)[2::]
            if cur[0] == 0:
                if int(tp10(tp10(k)), 2) > res:
                    return convert(num, base) if cur[1] == 0 else convert(int(tp10(tp10(k)), 2), base)
            if cur[0] == 1:
                if int(tp11(tp11(k)), 2) > res:
                    return convert(num, base) if cur[1] == 0 else convert(int(tp11(tp11(k)), 2), base)

    if var == 3:
        res = str(res)
        f = lambda num: str(num % cur[0]) + str(num % cur[1]) + str(num % cur[2])

        if cur_sort == 0:
            for num in range(10, 100):
                if f(num) == res:
                    return num
        if cur_sort == 1:
            for num in range(99, 9, -1):
                if f(num) == res:
                    return num

    if var == 4:
        for num in range(1, 255):
            new = ''
            for c in bin(num)[2::].zfill(8):
                if c == '1':
                    new += '0'
                else:
                    new += '1'
            if int(new.lstrip('0'), 2) - num == res:
                return num

    if var == 5:
        cnt = 0
        for num in range(cur[0], cur[1] + 1):
            out = []
            num = str(num)

            for i in range(len(num)):
                for j in range(len(num)):
                    if i != j:
                        out.append(int(num[i] + num[j]))
            if (max(out) - min(out)) == res:
                cnt += 1
        return cnt


def example(num, cur, cur_sort, var):
    if var == 1:
        tmp = {
            'первая': 0,
            'вторая': 1,
            'третья': 2,
            'четвёртая': 3
        }

        num = str(num)
        n1 = int(num[tmp[cur[0]]]) + int(num[tmp[cur[1]]])
        n2 = int(num[tmp[cur[2]]]) + int(num[tmp[cur[3]]])

        ex = {
            'n1': n1,
            'n2': n2,
            'num': num,
            'num1': num[tmp[cur[0]]],
            'num2': num[tmp[cur[1]]],
            'num3': num[tmp[cur[2]]],
            'num4': num[tmp[cur[3]]]
        }
        if cur_sort == 'убывания':
            ex['res'] = (str(max(n1, n2)) + str(min(n1, n2)))
        else:
            ex['res'] = (str(min(n1, n2)) + str(max(n1, n2)))

        return ex

    if var == 3:
        ex = {
            'res': (str(num % cur[0]) + str(num % cur[1]) + str(num % cur[2])),
            'n1': str(num % cur[0]),
            'n2': str(num % cur[1]),
            'n3': str(num % cur[2]),
            'num': num
        }

        return ex

    if var == 5:
        num = str(num)
        out = []

        for i in range(len(num)):
            for j in range(len(num)):
                if i != j:
                    out.append(int(num[i] + num[j]))
        ex = {
            'num': num,
            'max': max(out),
            'min': min(out),
            'res': max(out) - min(out)
        }

        return ex


for i in range(100):
    var = randint(1, 5)
    if var == 1:
        cur = ['первая', 'вторая', 'третья', 'четвёртая']
        shuffle(cur)
        cur_sort = ['убывания', 'возрастания'][randint(0, 1)]

        text = "Автомат получает на вход четырехзначное число. По этому числу строится новое число по следующим правилам.\n"
        text += f'1. Складываются { cur[0] } и { cur[1] }, а также { cur[2] } и { cur[3] } цифры исходного числа.\n'
        text += f'2. Полученные два числа записываются друг за другом в порядке {cur_sort} (без разделителей).\n'
        ex = example(randint(1000, 9999), cur, cur_sort, var)
        text += f"Пример. Исходное число: { ex['num'] }. Суммы: { ex['num1'] }+{ ex['num2'] } = { ex['n1'] };"
        text += f" { ex['num3'] }+{ ex['num4'] } = { ex['n2'] }. Результат: { ex['res'] }.\n"
        num = int(str(randint(10, 18)) + str(randint(10, 18)))
        ans = answer(num, cur, cur_sort, var)
        text += f"Укажите наименьшее число, в результате обработки которого, автомат выдаст число {num}.\n"
        text += f"Ответ: {ans}\n"
        if ans:
            f.write(text)

    if var == 2:
        cur_base = ['двоичной', 'восьмиричной', 'десятичной', 'шестнадцатиричной'][randint(0, 3)]
        tp1, tp2 = randint(0, 1), randint(0, 1)
        # tp1 - бит чётности или бит нечётности, tp2 - ищем результат или исходное число

        text = "На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.\n"
        text += "1) Строится двоичная запись числа N.\n"
        if tp1 == 0:
            text += "2) К этой записи дописывается справа бит чётности: 0, если в двоичном коде числа N было чётное число единиц, и 1, если нечётное.\n"
        else:
            text += "2) В конец числа (справа) дописывается 1, если число единиц в двоичной записи числа чётно, и 0, если число единиц в двоичной записи числа нечётно.\n"
        if tp1 == 0:
            text += "3) К полученному результату дописывается ещё один бит чётности.\n"
        else:
            text += "3) К этой записи справа дописывается 1, если остаток от деления количества единиц на 2 равен 0, и 0, если остаток от деления количества единиц на 2 равен 1.\n"
        text += "Полученная таким образом запись (в ней на два разряда больше, чем в записи исходного числа N) является двоичной записью искомого числа R. "
        num = randint(20, 500)

        if tp2 == 0:
            text += f"Укажите минимальное число N, после обработки которого с помощью этого алгоритма получается число, большее, чем { num }. В ответе это число запишите в десятичной системе.\n"
        else:
            text += f"Укажите минимальное число R, которое превышает { num } и может являться результатом работы алгоритма. В ответе это число запишите в { cur_base } системе.\n"
        ans = answer(num, [tp1, tp2], cur_base, var)
        text += f"Ответ: {ans}\n"
        f.write(text)

    if var == 3:
        tp1 = randint(0, 1)
        # Наименьшее или наибольшее число ищем

        cur = (randint(2, 9), randint(2, 9), randint(2, 9))
        while len(set(cur)) != 3:
            cur = (randint(2, 9), randint(2, 9), randint(2, 9))
        # Избегаем повторяющихся цифр в условии

        text = "Автомат получает на вход натуральное число X. По этому числу строится трёхзначное число Y по следующим правилам.\n"
        text += f"1. Первая цифра числа Y (разряд сотен) – остаток от деления X на { cur[0] }.\n"
        text += f"2. Вторая цифра числа Y (разряд десятков) – остаток от деления X на { cur[1] }.\n"
        text += f"3. Третья цифра числа Y (разряд единиц) – остаток от деления X на { cur[2] }.\n"

        ex = example(randint(11, 100), cur, 0, var)
        while ex['res'][0] == '0':
            ex = example(randint(11, 100), cur, 0, var)
        # В трёхзначном числе разряд сотен >=1
        text += f"Пример. Исходное число: { ex['num'] }. Остаток от деления на { cur[0] } равен { ex['n1'] }; остаток от деления на {cur[1]} равен {ex['n2']}; остаток от деления на {cur[2]} равен {ex['n3']}. Результат работы автомата: {ex['res']}.\n"

        num = randint(100, 888)
        while int(str(num)[0]) >= cur[0] or int(str(num)[1]) >= cur[1] or int(str(num)[2]) >= cur[2]:
            num = randint(100, 888)

        if tp1 == 0:
            text += f"Укажите наименьшее двузначное число, при обработке которого автомат выдаёт результат { num }.\n"
        if tp1 == 1:
            text += f"Укажите наибольшее двузначное число, при обработке которого автомат выдаёт результат { num }.\n"
        ans = answer(num, cur, tp1, var)
        text += f"Ответ: { ans }\n"

        if ans:
            f.write(text)

    if var == 4:
        text = "Автомат обрабатывает целое число N (0 ≤ N ≤ 255) по следующему алгоритму:\n"
        text += "1) Строится восьмибитная двоичная запись числа N.\n"
        text += "2) Все цифры двоичной записи заменяются на противоположные (0 на 1, 1 на 0).\n"
        text += "3) Полученное число переводится в десятичную запись.\n"
        text += "4) Из нового числа вычитается исходное, полученная разность выводится на экран.\n"
        num = randint(1, 128)
        text += f"Какое число нужно ввести в автомат, чтобы в результате получилось { num }?\n"
        ans = answer(num, 0, 0, var)
        text += f'Ответ: { ans }\n'
        if ans:
            f.write(text)

    if var == 5:
        a = randint(100, 500)
        b = randint(a + 100, a + 500)
        cur = (a, b)
        # Генерируем промежуток, в котором будем искать число

        text = "Автомат обрабатывает трёхзначное натуральное число N по следующему алгоритму.\n"
        text += "1. Из цифр, образующих десятичную запись N, строятся наибольшее и наименьшее возможные двузначные числа (числа не могут начинаться с нуля).\n"
        text += "2. На экран выводится разность полученных двузначных чисел.\n"

        num = randint(100, 999)
        while '0' in str(num):
            num = randint(100, 999)
        ex = example(num, 0, 0, var)
        text += f"Пример. Дано число N = { ex['num'] }. Алгоритм работает следующим образом.\n"
        text += f"1. Наибольшее двузначное число из заданных цифр – { ex['max'] }, наименьшее – { ex['min'] }.\n"
        text += f"2. На экран выводится разность { ex['max'] } – { ex['min'] } = { ex['res'] }.\n"
        num = randint(1, 80)
        text += f"Чему равно количество чисел N на отрезке [{ cur[0] }; { cur[1] }], в результате обработки которых на экране автомата появится число { num }?\n"

        ans = answer(num, cur, 0, var)
        text += f"Ответ: { ans }\n"
        if ans:
            f.write(text)
