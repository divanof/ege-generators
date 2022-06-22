import os
from random import randint
from functools import lru_cache

if not os.path.exists('../tasks'):
    os.mkdir('../tasks')
f = open('../tasks/5.txt', 'a')


# Func block
def bit0(num):
    # Бит чётности
    return int(bin(num)[2::] + str(bin(num)[2::].count('1') % 2), 2)


def bit1(num):
    # Обратный бит чётности
    return int(bin(num)[2::] + str(1 if bin(num)[2::].count('1') % 2 == 0 else 0), 2)


def f0(num):
    # Сделать чётное (*2)
    return num * 2


def f1(num):
    # Сделать нечётное (*2 + 1)
    return num * 2 + 1


def dec(num):
    # Увеличить число десятков
    return num + 10


def summ(num, k=0):
    # Сумма
    return num + k


def mult(num, k=1):
    return num * k


@lru_cache(None)
def answer(n, tar):
    global acts

    if n > tar:
        return 0

    if n == tar:
        return 1

    global bit0, bit1, f0, f1, dec, summ, mult
    funcs = {
        summ: [],
        mult: []
    }

    for key, value in acts.items():
        if key == 3:
            funcs[f0] = -1
        elif key == 4:
            funcs[f1] = -1
        elif key == 5:
            funcs[dec] = -1
        elif key == 6:
            funcs[bit0] = -1
        elif key == 7:
            funcs[bit1] = -1
        elif key == 1:
            for k in value:
                funcs[summ].append(k)
        elif key == 2:
            for k in value:
                funcs[mult].append(k)

    if len(funcs[summ]) == 0:
        del funcs[summ]
    if len(funcs[mult]) == 0:
        del funcs[mult]
    return sum([answer(i(n), tar) for i in funcs.keys() if i != summ and i != mult]) \
            + sum([answer(summ(n, i), tar) for i in funcs[summ]]) if summ in funcs else 0 \
            + sum([answer(mult(n, i), tar) for i in funcs[mult]]) if mult in funcs else 0


for i in range(10):
    cnt = randint(2, 5)
    # Количество возможных действий над числом
    n, tar = randint(1, 7), randint(15, 100)
    chk = 1
    # Счётчик для вывода действий в текст задания
    acts = {}
    a1 = []
    a2 = []
    # Ключи в этом словаре - действия: 1 - прибавить (убавить), 2 - умножить (разделить), 3 - сделать чётное,
    # 4 - сделать нечётное, 5 - увеличить (уменьшить) число десятков,
    # 6 - дописать бит чётности, 7 - дописать обратный бит чётности
    # Значения в словаре - то, на сколько изменяем число (если функция этого требует)
    # a1, a2 - списки, в которых будет лежать умножение и сложение (т.к. этих операций может быть >1)
    while len(acts) + len(a1) + len(a2) != cnt:
        cur = randint(1, 7)

        if cur not in acts.keys() and cur not in [1, 2]:
            acts[cur] = -1
        elif cur in [1, 2]:
            if cur == 1:
                k = randint(1, 3)
                if k not in a1:
                    a1.append(k)
            else:
                k = randint(2, 4)
                if k not in a2:
                    a2.append(k)
    if len(a1) > 0:
        acts[1] = a1
    if len(a2) > 0:
        acts[2] = a2

    text = "Исполнитель Калькулятор преобразует число на экране. "
    text += "У исполнителя есть команды, которым присвоены номера:\n"

    for key, value in acts.items():
        if key == 3:
            text += f"{chk}. Сделать из числа чётное (умножение числа на 2).\n"
            chk += 1
        elif key == 4:
            text += f"{chk}. Сделать из числа нечётное (умножение числа на 2 с прибавлением единицы).\n"
            chk += 1
        elif key == 5:
            text += f"{chk}. Увеличить число десятков на 1.\n"
            chk += 1
        elif key == 6:
            text += f"{chk}. Перевести число в 2-ю СС, дописать бит чётности "
            text += "(0, если число единиц в записи чётное, иначе 1), перевести обратно в 10-ю СС.\n"
            chk += 1
        elif key == 7:
            text += f"{chk}. Перевести число в 2-ю СС, дописать обратный бит чётности "
            text += "(1, если число единиц в записи чётное, иначе 0), перевести обратно в 10-ю СС.\n"
            chk += 1
        elif key == 1:
            for k in value:
                text += f"{chk}. Прибавить к числу {k}.\n"
                chk += 1
        elif key == 2:
            for k in value:
                text += f"{chk}. Умножить число на {k}.\n"
                chk += 1

    text += f"Программа для исполнителя – это последовательность команд. Сколько существует программ, которые число {n} преобразуют в число {tar}?\n"

    ans = answer(n, tar)
    text += f"Ответ: { ans }\n"
    if ans:
        f.write(text)
