import pygame
import sys

import nltk
from nltk.corpus import wordnet as wn
from nltk.wsd import lesk


grid_size = 6
cell_size = 55
gridwidth = grid_size * cell_size +110
grid_height = grid_size * cell_size
grid_color = (255, 255, 255)
box_color = (0, 255, 0)

grid_data = []
for i in range(grid_size):
    row = []
    for i in range(grid_size):
        row.extend(' ')
    grid_data.append(row)
grid_array = grid_data
# print(grid_array)
pygame.init()

screen = pygame.display.set_mode((gridwidth, grid_height))
pygame.display.set_caption("Box Table")

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

    # data =
for i in grid_data:
    print(i)

horizen_lst = []
word = ''
for i in grid_data:
    for j in i:
        if j != ' ':
            word += str(j)
        elif j == ' ' and len(word) > 1:
            horizen_lst.append(word)
            # print(word)
            word = ''
            pass

print('horizon >>', horizen_lst)

vertical_lst = []
word = ''
for i in range(len(grid_data)):
    for j in range(len(grid_data)):
        if grid_data[j][i] != ' ':
            word += str(grid_data[j][i])
        elif grid_data[j][i] == ' ' and len(word) > 1:
            vertical_lst.append(word)
            # print(word)
            word = ''
            pass
print('vertical >>', vertical_lst)


for i in horizen_lst:
    for ss in wn.synsets(str(i)):
        print(ss, ss.definition())

pygame.quit()
sys.exit()
