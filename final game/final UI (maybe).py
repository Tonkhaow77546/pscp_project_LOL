import pygame, sys
from button import Button
from League_of_letter_final import main_game
pygame.init()

SCREEN = pygame.display.set_mode((1920, 1060))
pygame.display.set_caption("League of Letter")

## Sound
def music():
    pygame.mixer.init()
    pygame.mixer.music.load("UI/music1.mp3")
    pygame.mixer.music.play(-1)
def click():
    """run soud click"""
    pygame.mixer.music.load("UI/click.mp3")
    pygame.mixer.music.play()

## Credit
CDBG = pygame.image.load("UI/credit.png")
CDBG = pygame.transform.scale(CDBG, (1920, 1060))

## Background
BG = pygame.image.load("UI/Background.png")
BG = pygame.transform.scale(BG, (1920, 1060))

## bottonplay
botton_play = pygame.image.load("UI/Start_2.png")
botton_play = pygame.transform.scale(botton_play, (300,80))

## bottonmode
botton_mode = pygame.image.load("UI/Mode.png") 
botton_mode = pygame.transform.scale(botton_mode, (300,500))

## bottonsetting
botton_setting = pygame.image.load("UI/Setting.png")
botton_setting = pygame.transform.scale(botton_setting, (80,100))

## bottoncredit
botton_credit = pygame.image.load("UI/Credits_2.png")
botton_credit = pygame.transform.scale(botton_credit, (180,60))

## EjudgeAvatar
ejudge_avatar = pygame.image.load("UI/ejudgeavatar.png")
ejudge_avatar = pygame.transform.scale(ejudge_avatar, (300,300))

def playgame():
    """playgame"""
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("Gray")

        OPTIONS_TEXT = get_font(45).render("This is game", True, "Aquamarine")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=pygame.image.load("UI/Quit Rect.png"), pos=(640, 460), 
                            text_input="Back", font=get_font(75), base_color="Blue", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
        pygame.display.update()
    
def setting():
    """settingmenu"""
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("Gray")

        OPTIONS_TEXT = get_font(45).render("setting menu", True, "Aquamarine")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=pygame.image.load("UI/Quit Rect.png"), pos=(640, 460), 
                            text_input="Back", font=get_font(75), base_color="Blue", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
        pygame.display.update()

def credit():
    """credit"""
    while True:
        
        SCREEN.blit(CDBG, (0, 0))

        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        OPTIONS_TEXT = get_font(50).render("Credit", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 90))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=pygame.image.load("UI/Quit Rect.png"), pos=(640, 860), 
                            text_input="Back", font=get_font(75), base_color="Blue", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
        pygame.display.update()

# Returns Press-Start-2P in the desired size
def get_font(size): 
    return pygame.font.Font("font.ttf", size)

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("League of Letter", True, "White")
        MENU_RECT = MENU_TEXT.get_rect(center=(960, 500))

        PLAY_BUTTON = Button(botton_play , pos=(960, 600),  ##ปุ่ม start size < 400 x 200 , > 250 x 70
                            text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="Black")
        MODE_BUTTON = Button(botton_mode, pos=(640, 620), #ปุ่ม option size < ที่ใส่ไปแล้วไม่น่าเกลียด
                            text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="Black")
        SETTING_BUTTON = Button(botton_setting, pos=(1200, 60), #ปุ่ม option size < ที่ใส่ไปแล้วไม่น่าเกลียด
                            text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="Black")
        CREDIT_BUTTON = Button(botton_credit, pos=(125, 60), #ปุ่ม option size < ที่ใส่ไปแล้วไม่น่าเกลียด
                            text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="Black")
        
        SCREEN.blit(MENU_TEXT, MENU_RECT)
        SCREEN.blit(ejudge_avatar, (810, 150))

        for button in [PLAY_BUTTON, CREDIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        click()
                        main_game()
                    #if SETTING_BUTTON.checkForInput(MENU_MOUSE_POS):
                        #click()
                        #setting()
                    if CREDIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        click()
                        credit()

        pygame.display.update()

main_menu()
