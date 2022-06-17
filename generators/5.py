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

        for i in range(1, 10000):
            k = bin(i)[2::]
            if cur[0] == 0:
                if int(tp10(tp10(k)), 2) > res:
                    return convert(i, base) if cur[1] == 0 else convert(int(tp10(tp10(k)), 2), base)
            if cur[0] == 1:
                if int(tp11(tp11(k)), 2) > res:
                    return convert(i, base) if cur[1] == 0 else convert(int(tp11(tp11(k)), 2), base)


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
    if var == 2:
        pass


for i in range(10):
    var = randint(1, 2)
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
