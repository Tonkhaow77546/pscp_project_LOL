import pygame
import sys
import random
import string
import copy

numtable = 8
area = 80
wide = (numtable*area) + (area*4)
height = numtable*area
linecolor = (255, 255, 255)
boxcolor = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode((wide, height))
pygame.display.set_caption("Test")

table = [["" for _ in range(numtable)] for _ in range(numtable)]
newtable = copy.deepcopy(table)


print('-------------------------------------')
for i in newtable:
    print(i)
print('-------------------------------------')


def random_letter():
    return random.choice(string.ascii_lowercase)


word_table = [random_letter() for _ in range(numtable-2)]
word_table.extend(['reset', 'summit'])
print(word_table)
new_word = list(word_table)
print(new_word)
wordclick, mainclick = False, False

running = True
word_clicked = []
word_applied = dict()
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # click word table
            if numtable * area + 100 <= mouse_x < numtable * area + 100 + area:
                where_click = (mouse_y // area)
                print(where_click)
                if 0 <= where_click < numtable-2:
                    wordclick = where_click
                    mainclick = word_table[wordclick]

                # reset word position
                elif where_click == numtable-2:
                    print('reset')
                    print(word_applied)
                    clicked_pos_table = list(word_applied.keys())
                    clicked_pos_word = list(word_applied.values())
                    print('table =', clicked_pos_table)
                    print('word =', clicked_pos_word)
                    filling = []
                    for i in clicked_pos_table:
                        temp_pos = (i).split(',')
                        print('temp_pos ==', temp_pos)
                        table[int(temp_pos[0])][int(temp_pos[1])] = 0

                        for i in range(len(word_table)):
                            if word_table[i] == '':
                                filling.append(i)
                        print('filling =', filling)
                        for i in range(len(clicked_pos_word)):
                            word_table[filling[i]] = clicked_pos_word[i]
                            print(word_table)
                    word_clicked = []
                    word_applied = dict()
                    pass
                # summit word position
                elif where_click == numtable-1:
                    print('summit')
                    # print(table)
                    print(word_table)
                    print(word_clicked)
                    for i in word_clicked:
                        word_table[i] = random_letter()
                    summit_stage = True
                #print word in row and column for check meaning
                    #column
                    for x in range(numtable):
                        word = ""
                        for y in range(numtable):
                            word += table[x][y]
                        print("word column", word)
                    #row
                    for x in range(numtable):
                        word = ""
                        for y in range(numtable):
                            word += table[y][x]
                        print("word row", word)
                    word_applied = dict()
                    word_clicked = []
                    pass

        # click main table
            elif 0 <= mouse_x < numtable * area and 0 <= mouse_y < numtable * area:
                if wordclick is not False:
                    where_main, where_click = mouse_x // area, mouse_y // area
                    if 0 <= where_main < numtable and 0 <= where_click < numtable:
                        if table[where_main][where_click] in [0, '']:
                            table[where_main][where_click] = mainclick
                            if word_table[wordclick] == '':
                                pass
                            else:
                                word_table[wordclick] = ''
                                word_clicked.append(wordclick)
                                word_applied.update(
                                    {str(where_main)+',' + str(where_click): mainclick})
                        wordclick, mainclick = False, False

    summit_stage = False
    reset_stage = False
    screen.fill((0, 0, 0))
    # table
    for x in range(numtable):
        for y in range(numtable):
            pygame.draw.rect(screen, linecolor,
                             (x * area, y * area, area, area), 1)
            if table[x][y] != 0:
                text = pygame.font.Font(None, 50).render(
                    table[x][y], True, (255, 0, 0))
                screen.blit(text, (x * area + area // 3, y * area + area // 3))
    if newtable != table:
        '''for i in table:
            print(i)
        print('---------------------------------')'''
        newtable = copy.deepcopy(table)
    # word table
    for y in range(numtable):
        pygame.draw.rect(screen, linecolor, (numtable *
                         area + 100, y * area, area, area), 1)
        text = pygame.font.Font(None, 50).render(
            word_table[y], True, (255, 0, 0))
        screen.blit(text, (numtable * area + 150, (y * area) + 30))
    if list(word_table) != new_word:
        for i in table:
            print(i)
        print('---------------------------------')
        new_word = list(word_table)
    pygame.display.flip()

pygame.quit()
sys.exit()
