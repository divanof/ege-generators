import random
import os

if not os.path.exists('../tasks'):
    os.mkdir('../tasks')
f = open('../tasks/12.txt', 'a')

var = ['''7
Дана программа для исполнителя Редактор:
ПОКА нашлось ({0}) ИЛИ нашлось ({1})
  ЕСЛИ нашлось ({1})
    ТО заменить ({1}, {2})
    ИНАЧЕ заменить ({0}, {3})
  КОНЕЦ ЕСЛИ
КОНЕЦ ПОКА
Дана строка, состоящая из {4} цифр {5}. Сколько {6} было удалено за время обработки строки по этой программе?''',

'''7
Дана программа для исполнителя Редактор:
НАЧАЛО
 ПОКА нашлось ({0})
   заменить ({1}, {2})
   заменить ({3}, {4})
 КОНЕЦ ПОКА
КОНЕЦ
Какая строка получится в результате применения приведённой ниже программы к строке, состоящей из {5} цифр {6}?''',

'''9
Дана программа для исполнителя Редактор:
НАЧАЛО
ПОКА нашлось ({0})
    заменить ({1}, {2})
    заменить ({3}, {4})
КОНЕЦ ПОКА
КОНЕЦ
Какая строка получится в результате применения приведённой программы к строке вида {5}…{5}{6}…{6} ({7} {5} и {8} {6})?
'''
       ]


def gen(num, amo=1, out='p'):
    for _ in range(amo):
        f = open('../tasks/12.txt', 'a')
        blp = var[num - 1]
        kol = int(blp[0])
        blp = blp[1:]
        s = []
        for _ in range(kol):
            s.append(str(random.randrange(0, 9)))
        if num == 1:
            s[0] *= random.randrange(3, 6)
            s[1] *= random.randrange(3, 6)
            while s[0] == s[1]:
                s[1] = str(random.randrange(0, 9)) * random.randrange(3, 6)
            s[2] = s[0][0] * random.randrange(1, 3)
            s[3] = s[1][0] * random.randrange(1, 3)
            s[4] = random.randrange(100, 700)
            s[5] = random.choice([s[0][0], s[1][0]])
            s[6] = random.choice([s[0][0], s[1][0]])
            blp = blp.format(s[0], s[1], s[2], s[3], s[4], s[5], s[6])

            d = s[5] * int(s[4])
            kol = 0
            unit = 2 if s[6] in s[2] else 3

            while s[0] in d or s[1] in d:
                if s[1] in d:
                    d = d.replace(s[1], s[2], 1)
                    if unit == 2:
                        kol += len(s[unit])
                else:
                    d = d.replace(s[0], s[3], 1)
                    if unit == 3:
                        kol += len(s[unit])
            if out == 'p':
                print(blp + '\n\nОтвет: ' + str(kol) + '\n')
            if out == 'f':
                f.write(blp + '\n\nОтвет: ' + str(kol) + '\n')
        if num == 2:
            s[0] *= random.randrange(6, 8)
            s[1] = s[0][0] * random.randrange(4, 6)
            s[2] = str(random.randrange(0, 9)) * random.randrange(2, 4)
            while s[0][0] == s[2][0]:
                s[2] = str(random.randrange(0, 9)) * random.randrange(2, 4)
            s[3] = s[2][0] * random.randrange(1, 3)
            s[4] = s[0][0] * random.randrange(2, 4)
            s[5] = random.randrange(100, 700)
            s[6] = random.choice([s[0][0], s[1][0]])
            blp = blp.format(s[0], s[1], s[2], s[3], s[4], s[5], s[6])

            d = s[6] * int(s[5])

            if len(s[4]) < len(s[1]):
                print(blp)
                while s[0] in d:
                    d = d.replace(s[1], s[2], 1)
                    d = d.replace(s[3], s[4], 1)
            else:
                d = 'ЗАДАЧА С БЕСКОНЕЧНЫМ ЦИКЛОМ'
            if out == 'p':
                print(blp + '\n\nОтвет: ' + d + '\n')
            if out == 'f':
                f.write(blp + '\n\nОтвет: ' + d + '\n')
        if num == 3:
            s[0] *= random.randrange(6, 8)
            s[1] = s[0]
            s[2] = str(random.randrange(0, 9)) * random.randrange(2, 4)
            while s[0][0] == s[2][0]:
                s[2] = str(random.randrange(0, 9)) * random.randrange(2, 4)
            s[3] = s[2][0] * random.randrange(1, 3)
            s[4] = s[0][0] * random.randrange(2, 4)
            s[5] = random.choice([s[0][0], s[2][0]])
            s[6] = random.choice([s[0][0], s[1][0]])
            s[7] = random.randrange(1, 100)
            s[8] = random.randrange(1, 100)
            blp = blp.format(s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7], s[8])

            d = s[5] * int(s[7]) + s[6] * int(s[8])

            if len(s[4]) < len(s[1]):
                while s[0] in d:
                    d = d.replace(s[1], s[2], 1)
                    d = d.replace(s[3], s[4], 1)
            else:
                d = 'ЗАДАЧА С БЕСКОНЕЧНЫМ ЦИКЛОМ'
            if out == 'p':
                print(blp + '\n\nОтвет: ' + d + '\n')
            if out == 'f':
                f.write(blp + '\n\nОтвет: ' + d + '\n')


gen(3, amo=10, out='p')
