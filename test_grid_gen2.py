import pygame
import sys

GRID_SIZE = 5
CELL_SIZE = 55
GRID_WIDTH = GRID_SIZE * CELL_SIZE
GRID_HEIGHT = GRID_SIZE * CELL_SIZE
GRID_COLOR = (255, 255, 255)
BOX_COLOR = (0, 255, 0)

grid_data = []
for i in range(GRID_SIZE):
    row = []
    for i in range(GRID_SIZE):
        row.extend(' ')
    grid_data.append(row)
grid_array = grid_data
# print(grid_array)
pygame.init()

screen = pygame.display.set_mode((GRID_WIDTH, GRID_HEIGHT))
pygame.display.set_caption("Box Table")

table = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            grid_x = mouse_x // CELL_SIZE
            grid_y = mouse_y // CELL_SIZE
            print(f"possition ({grid_x}, {grid_y})")
            vocab = str(input())
            table[grid_x][grid_y] = 1

    screen.fill((0, 0, 0))

    # make table
    for x in range(GRID_SIZE):

        for y in range(GRID_SIZE):

            pygame.draw.rect(screen, GRID_COLOR, (x * CELL_SIZE,
                             y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 2)
            if table[x][y] == 1:
                pygame.draw.rect(
                    screen, BOX_COLOR, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                grid_data[grid_y][grid_x] = vocab[0]

    pygame.display.flip()

    # data =
for i in grid_data:
    print(i)


pygame.quit()
sys.exit()
