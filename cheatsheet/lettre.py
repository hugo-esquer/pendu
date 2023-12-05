import pygame

pygame.init()

WIDTH, HEIGHT = 900, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0, 0, 0)

LETTER_FONT = pygame.font.SysFont("comicsans", 40)


LETTER_WIDTH = 20
GAP = 15
letters = []
startx = round((WIDTH - (LETTER_WIDTH * 2 + GAP) * 13) / 2)
starty = 350
A = 97
for i in range(26):
    x = startx + ((LETTER_WIDTH * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + LETTER_WIDTH * 2))
    letters.append([x, y, chr(A + i), True])

def draw():
    win.fill((255, 255, 255))

    for letter in letters:
        x, y, ltr, visible = letter
        text = LETTER_FONT.render(ltr, 1, BLACK)
        win.blit(text, (x, y))

    pygame.display.update()


run = True

while run:

    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
        