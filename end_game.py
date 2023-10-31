'''end game'''
import pygame
import sys
import math
#from button import Button
#from nltk.corpus import wordnet as wn
#from nltk.wsd import lesk

#***********เปลี่ยน จาก league_of_letters_1 เป็น league_of_letters*********
#from testspace3 import main_game
##from league_of_letters_1 import used_word as answer
#from league_of_letters_1 import total_score as final_score


pygame.init()
SCREEN = pygame.display.set_mode((1920, 1060))
pygame.display.set_caption("League of Letter")


word_lenth = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
#word_lenth = ['Hello','GYM','paint','pokemon']
#word_lenth = ['Hello', 'gym']
def endgame():
    while True:
        SCREEN.fill("#3c8dbc")#สีเมนู problem ใน ejudge
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('111')
                pygame.quit()
                sys.exit()

        #pygame.display.flip()
        
        #screen for meaing
        pygame.draw.rect(SCREEN,(239,204,162),(100 , 150 , 1200 , 800))
        counter = 0
        '''for i in word_lenth:
            for ss in wn.synsets(str(i)):
                meaning = (ss, ss.definition())
                print(meaning)
                text = pygame.font.Font(None, 30).render(str(meaning), True, (255, 0, 0))
                SCREEN.blit(text,(110,165+(counter*25)))
                counter +=1
                break'''

        #showing score
        total_score=99
        pygame.draw.circle(SCREEN, (255,0,0), (1500,225), (100))
        text = pygame.font.Font(None, 100).render(str(total_score), True, (0, 255, 0))
        SCREEN.blit(text,(1460,200))
        
        #try again button
        pygame.draw.circle(SCREEN, (255,0,0), (1750,225), (100))
        text = pygame.font.Font(None, 50).render(str('Try Again'), True, (0, 255, 0))
        SCREEN.blit(text,(1680,215))

        #screen for word
        for i in range(len(word_lenth)):
            if i >= len(word_lenth)/2:
                pygame.draw.rect(SCREEN,(239,204,162),(1675 , 350+((i-math.ceil(len(word_lenth)/2))*35) , 200 , 30))
                text = pygame.font.Font(None, 30).render(str(word_lenth[i]), True, (255, 0, 0))
                SCREEN.blit(text,(1675 , 360+((i-math.ceil(len(word_lenth)/2))*35)))
            else:
                pygame.draw.rect(SCREEN,(239,204,162),(1400 , 350+(i*35) , 200 , 30))
                text = pygame.font.Font(None, 30).render(str(word_lenth[i]), True, (255, 0, 0))
                SCREEN.blit(text,(1400 , 360+(i*35)))

        pygame.display.update()


endgame()
