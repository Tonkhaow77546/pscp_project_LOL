import pygame, sys
from button import Button

pygame.init()

grid_size = 6
cell_size = 55
gridwidth = 1280
grid_height = 720
grid_color = (255, 255, 255)
box_color = (0, 255, 0)


SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("UI/Background.png") ## Background

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size) 

def play():
    screen = pygame.display.set_mode((gridwidth, grid_height))
    pygame.display.set_caption("Game Play")

    table = [[0 for _ in range(grid_size)] for _ in range(grid_size)]

    running = True


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                grid_x = mouse_x // cell_size
                grid_y = mouse_y // cell_size
                print(f"possition ({grid_x}, {grid_y})")
                vocab = str(input())
                table[grid_x][grid_y] = 1

        screen.fill((0, 0, 0))

        # make table
        for x in range(grid_size):

            for y in range(grid_size):

                pygame.draw.rect(screen, grid_color, (x * cell_size,
                                y * cell_size, cell_size, cell_size), 2)
                if table[x][y] == 1:
                    pygame.draw.rect(
                        screen, box_color, (x * cell_size, y * cell_size, cell_size, cell_size))
                    grid_data[grid_y][grid_x] = vocab[0]
            
        #make word table
        for l in range(grid_size):
            pygame.draw.rect(screen, grid_color, (grid_size * cell_size + 55, l * cell_size, cell_size, cell_size), 2)

        pygame.display.flip()
            

        pygame.display.update()
        
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("Gray")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Aquamarine")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=pygame.image.load("UI/Quit Rect.png"), pos=(640, 460), 
                            text_input="Hard", font=get_font(75), base_color="Blue", hovering_color="Green")

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

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("UI/test.png"), pos=(640, 250), ##ปุ่ม start size < 400 x 200 , > 250 x 70
                            text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White") 
        OPTIONS_BUTTON = Button(image=pygame.image.load("UI/Options Rect.png"), pos=(640, 400), #ปุ่ม option size < ที่ใส่ไปแล้วไม่น่าเกลียด
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("UI/Quit Rect.png"), pos=(640, 550), ##ปุ่ม Quit size < 400 x 200 , > 250 x 70
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()








