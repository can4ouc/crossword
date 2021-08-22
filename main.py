import pygame

pygame.init()
words = ['дом', 'кошка', 'мышь', 'питон', 'кот']


def prepareList(ls: list):
    ls.insert(0, ['*'] * (len(test[0]) + 2))
    ls.append(['*'] * (len(test[1]) + 1))
    for i in range(1, len(test)-1):
        ls[i].insert(0, '*')
        ls[i].append('*')
    ls[-1].append('*')


test = [
    ['д', 'к', 'о', 'ш', 'м'],
    ['о', 'м', 'ы', 'к', 'ы'],
    ['ы', 'ы', 'ы', 'а', 'ш'],
    ['к', 'о', 'т', 'б', 'ь'],
    ['п', 'и', 'т', 'о', 'н'],
]
Height = ((len(test)) + len(words)) * 26
Width = 26 * len(test[0])

prepareList(test)

for i in test:
    print(i)


def search(letter, line_index=None, bukva_index=None):
    global wrong
    if not line_index and not bukva_index:
        for line in test:
            for bukva in line:
                if letter == bukva:
                    if not (test.index(line), line.index(bukva)) in wrong:
                        return (test.index(line), line.index(bukva))
                    else:
                        continue
        return None
    else:

        if letter == test[line_index][bukva_index - 1]:
            return line_index, bukva_index - 1
        elif letter == test[line_index - 1][bukva_index]:
            return line_index - 1, bukva_index
        elif letter == test[line_index + 1][bukva_index - 1]:
            return line_index, bukva_index + 1
        elif letter == test[line_index + 1][bukva_index]:
            return line_index + 1, bukva_index
        elif letter == test[line_index][bukva_index + 1]:
            return line_index, bukva_index + 1
        elif letter == test[line_index - 1][bukva_index + 1]:
            return line_index - 1, bukva_index + 1
        elif letter == test[line_index + 1][bukva_index + 1]:
            return line_index + 1, bukva_index + 1
        elif letter == test[line_index - 1][bukva_index - 1]:
            return line_index - 1, bukva_index - 1
        else:
            return 'бебе'


wrong = []
ind_ans = []


def way_search(word: str):
    global ind_ans
    global wrong
    for letter in range(len(word)):
        if letter == 0:
            a = search(word[letter])
            ind_ans.append(a)
        else:
            a = search(word[letter], a[0], a[1])
            if a == 'бебе':
                wrong.append(ind_ans[0])
                ind_ans.clear()
                return way_search(word)
            ind_ans.append(a)
    wrong.clear()

    return ind_ans

for word in words:
    print(word, way_search(word))
    ind_ans.clear()
