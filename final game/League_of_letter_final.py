import pygame
import sys
import random
import nltk
import math
from button import Button
from nltk.corpus import wordnet as wn
from nltk.wsd import lesk

used_word = []
total_score = 0
pass_word = []
letter_count = {"A": 5, "B": 5, "C": 5, "D": 5, "E": 5, "F": 5, "G": 5, "H": 5, "I": 5, \
                        "J": 5, "K": 5, "L": 5, "M": 5, "N": 5, "O": 5, "P": 5, "Q": 5, "R": 5, \
                        "S": 5, "T": 5, "U": 5, "V": 5, "W": 5, "X": 5, "Y": 5, "Z": 5}


def inside(x, y):
    
    check = (x - 1775)**2 + (y - 125)**2 #แก้ ตำแหน่ง*
    if check <= 100**2:
        print("อยู่ในวงกลมนะ")
        return 1
    return 0

def endgame():
    SCREEN = pygame.display.set_mode((1920, 1060))
    pygame.display.set_caption("League of Letter")
    background = pygame.image.load("End Game UI.png")
    background = pygame.transform.scale(background,(1920, 1060))
    SCREEN.blit(background,(0,0))
    pygame.init()
    global total_score, letter_count
    
    while True:
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('111')
                pygame.quit()
                sys.exit()
        #screen for meaing
        counter = 0
        if len(set(pass_word)) > 0:
            for i in set(pass_word):
                for ss in wn.synsets(str(i)):
                    meaning = (ss, ss.definition())
                    lenth = len(meaning[1])
                    space = 0
                    if lenth >= 50:
                        text = pygame.font.Font(None, 30).render(str(i)+'  '+str(meaning[0])+str(meaning[1][space:space + 50]), True, (255, 0, 0))
                        while space <= lenth:
                            space += 50
                            counter += 1
                            text = pygame.font.Font(None, 30).render(str(meaning[1][space:space + 50]), True, (255, 0, 0))
                            SCREEN.blit(text,(110,180+(counter*25)))
                            
                        pass
                    else:
                        text = pygame.font.Font(None, 30).render(str(meaning), True, (255, 0, 0))
                        SCREEN.blit(text,(110,180+(counter*25)))
                    counter +=1
                    break

        #showing score
        text = pygame.font.Font(None, 100).render(str(total_score), True, (0, 255, 0))
        SCREEN.blit(text,(1460,105))
        
        #try again button
        if event.type == pygame.MOUSEBUTTONDOWN:
            where = pygame.mouse.get_pos()
            pygame.draw.circle(SCREEN, (0,255,0), (1775,125), (100))#แก้ ตำแหน่ง*
            if 1675 <= where[0] <= 1875 and 25 <= where[1] <= 225:
                if inside(where[0], where[1]) == 1:
                    total_score = 0
                    letter_count = {"A": 5, "B": 5, "C": 5, "D": 5, "E": 5, "F": 5, "G": 5, "H": 5, "I": 5, \
                        "J": 5, "K": 5, "L": 5, "M": 5, "N": 5, "O": 5, "P": 5, "Q": 5, "R": 5, \
                        "S": 5, "T": 5, "U": 5, "V": 5, "W": 5, "X": 5, "Y": 5, "Z": 5}
                    main_game()# ให้ไป maingame*********
                    print("ไปเล่นใหม่นะ")
                    break
                else:
                    pass

        #screen for word
        for i in range(len(used_word)):
            if i >= len(used_word)/2:
                text = pygame.font.Font(None, 30).render(str(used_word[i]), True, (255, 0, 0))
                SCREEN.blit(text,(1675 , 275+((i-math.ceil(len(used_word)/2))*45.5)))#แก้ ตำแหน่ง*
                
            else:
                text = pygame.font.Font(None, 30).render(str(used_word[i]), True, (255, 0, 0))
                SCREEN.blit(text,(1400 , 275+(i*45.5)))#แก้ ตำแหน่ง*

        pygame.display.update()





def main_game():
    
    
    numtable = 12
    area = 80
    linecolor = (255, 0, 0)
    summit_time = 3

    screen = pygame.display.set_mode((1920, 1060))
    pygame.display.set_caption("League of Letter")
    background = pygame.image.load("In Game UI.png")
    background = pygame.transform.scale(background,(1920, 1025))
    screen.blit(background,(0,0))
    pygame.init()

    

    table = [["" for _ in range(numtable)] for _ in range(numtable)]
    newtable = table.copy()

    print('-------------------------------------')
    for i in newtable:
        print(i)
    print('-------------------------------------')

    def random_letter():
        key, value = random.choice(list(letter_count.items()))
        if value == 1:
            letter_count.pop(key)
            #print(letter_count)
            return key
        letter_count[key] -= 1
        #print(letter_count)
        return key

    word_table = [random_letter() for _ in range(numtable-2)]
    word_table.extend(['', ''])
    print(word_table)
    new_word = list(word_table)
    print(new_word)
    wordclick, mainclick = False, False

    running = True
    word_clicked = []
    word_applied = dict()
    reset = False
    global used_word1
    global total_score
    global pass_word

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print(mouse_x,mouse_y)

                reset = False
                old_table = table
                # click word table
                if 1180 <= mouse_x < 1270:
                    where_click = ((mouse_y-50) // area)
                    print(where_click)
                    if 0 <= where_click < numtable-2:
                        wordclick = where_click
                        mainclick = word_table[wordclick]
                        summit_stage = True
                    
                    # reset word position
                    elif where_click == numtable-2:
                        
                        print(word_applied)
                        clicked_pos_table = list(word_applied.keys())
                        clicked_pos_word = list(word_applied.values())
                        print('table =', clicked_pos_table)
                        print('word =', clicked_pos_word)
                        filling = []
                        for i in clicked_pos_table:
                            temp_pos = (i).split(',')
                            print('temp_pos ==', temp_pos)
                            table[int(temp_pos[0])][int(temp_pos[1])] = ""
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
                   

                    elif (where_click == numtable-1) and summit_stage == True:
                        total_score = 0
                        summit_stage = False
                    # print word in row and column for check meaning
                        # column
                        for i in range(len(table)):
                            column_word = ''
                            for j in range(len(table)):
                                word = table[j][i]
                                if word == '' and (len(column_word) >= 2) and column_word not in used_word:
                                    used_word.append(column_word)
                                    print('column_word : {}'.format(column_word))
                                    column_word = ''
                                    pass
                                elif word != '':
                                    column_word += word
                            
                        # row
                        for i in table:
                            row_word = ''
                            for j in i:
                                print(row_word)
                                if(j == '') and (len(row_word) >= 2) and row_word not in used_word:
                                    used_word.append(row_word)
                                    print('row_word : {}'.format(row_word))
                                    row_word = ''
                                    pass
                                elif j != '':
                                    row_word += j
                                


                        
                        print('summit')
                        print('used_word : {}'.format((used_word)))
                        print('used_word : {}'.format(set(used_word)))
                        pass_check = False
                        if reset == False:
                            for i in (set(used_word)):
                                if reset == True:
                                    break
                                print('i = ',i)
                                
                                for ss in wn.synsets(str(i))[:3]:
                                    
                                    if (len(ss.definition()) >= 3) :
                                        print('Pass')
                                        print(ss, ss.definition())
                                        pass_check = True
                                    else:
                                        print('fail')
                                if pass_check == True:
                                    total_score+= len(str(i))
                                    pass_word.append(i)
                                    pass_check = False


                            summit_time -= 1
                            if summit_time == 0:
                                endgame()
                                pass

                        if reset == False:
                            print(word_table)
                            print(word_clicked)
                            for i in word_clicked:
                                word_table[i] = random_letter()

                            word_applied = dict()
                            word_clicked = []
                            print('Your Score Now : {}'.format(total_score))
                            pass

            # click main table
                elif 50 <= mouse_x < 1010 and 50 <= mouse_y < 1010:
                    if wordclick is not False:
                        where_main, where_click = (mouse_x-50) // area, (mouse_y-50) // area
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

        #screen.fill((0, 0, 0))#***********
        screen.blit(background,(0,0))
        # table
        for x in range(numtable):
            for y in range(numtable):
                #pygame.draw.rect(screen, linecolor,((x * area) + 50, (y * area) + 50, area, area), 3)
                text = pygame.font.Font(None, 50).render(table[x][y], True, (255, 0, 0))
                screen.blit(text, ((x * area + area // 3) + 45,( y * area + area // 3) + 45))
        if newtable != table:
            '''for i in table:
                print(i)
            print('---------------------------------')'''

            newtable = table.copy()
        # word table
        for y in range(numtable):
            #pygame.draw.rect(screen, linecolor, (numtable *area + 225, y * area+50, area, area), 1)
            text = pygame.font.Font(None, 50).render(word_table[y], True, (255, 0, 0))
            screen.blit(text, (numtable * area + 250, (y * area) + 80))
        if list(word_table) != new_word:
            for i in table:
                '''print(i)
            print('---------------------------------')'''
            new_word = list(word_table)
        
        # show score
        
        text = pygame.font.Font(None, 100).render(str(total_score), True, (0, 255, 0))
        screen.blit(text, (1720,750))


        # summit time
        #pygame.draw.circle(screen, (255,0,0), (1700,950), (5))
        text = pygame.font.Font(None, 100).render(str(summit_time), True, (0, 255, 0))
        screen.blit(text, (1720,920))
        pygame.display.update()

    pygame.quit()
    sys.exit()

#main_game()
#endgame()
