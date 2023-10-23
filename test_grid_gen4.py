import pygame
import sys

numtable = 12
area = 80
pygame.init()

screen = pygame.display.set_mode((1920, 1060))
pygame.display.set_caption("Box Table")


running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    for x in range(numtable):
            for y in range(numtable):
                pygame.draw.rect(screen, (255, 255, 255),((x * area) + 50, (y * area) + 50, area, area), 3)
    for y in range(numtable):
            pygame.draw.rect(screen, (255, 255, 255), (numtable *area + 225, y * area+50, area, area), 1)
    pygame.display.flip()
pygame.quit()
sys.exit()
