import time
from copy import deepcopy
import pygame

pygame.init()
words = []
with open("word_rus.txt",'r') as file_handler:
    for line in file_handler:
        words.append(line.strip('\n'))

print(words)

pygame.font.init()  # you have to call this at the start,
# if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 30)


def prepareList(ls: list):
    ls.insert(0, ['*'] * (len(test[0]) + 2))
    ls.append(['*'] * (len(test[1]) + 1))
    for i in range(1, len(test) - 1):
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
Height = (((len(test)) + len(words)) * 36)
Width = (100 * len(test[0]))
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Crossword")
clock = pygame.time.Clock()
FPS = 30  # частота кадров в секунду
WHITE = pygame.color.Color('white')
RED = pygame.color.Color('red')

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
            return None


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
            if a == None:
                wrong.append(ind_ans[0])
                ind_ans.clear()
                return way_search(word)
            ind_ans.append(a)
    wrong.clear()

    return ind_ans


all_way = []
for word in words:
    try:
        way = way_search(word)
        way1 = deepcopy(way)
        all_way.append(way1)
    except:
        pass
    ind_ans.clear()

print(all_way)
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    # Рендеринг
    screen.fill(WHITE)
    for line in range(len(test)):
        for letter in range(len(test[line])):
            bukva = myfont.render(test[line][letter], False, (0, 0, 0))
            screen.blit(bukva, (letter * 30, line * 30))
    for word in all_way:
        for coord in range(len(word) - 1):
            pygame.draw.line(screen, RED, (word[coord][1] * 30 + 5, word[coord][0] * 30 + 10),
                             (word[coord + 1][1] * 30 + 5, word[coord + 1][0] * 30 + 10))
            pygame.display.flip()
            time.sleep(0.1)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
