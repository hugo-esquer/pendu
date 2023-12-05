import pygame

pygame.init()

WIDTH, HEIGHT = 900, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0, 0, 0)

LETTER_FONT = pygame.font.SysFont("comicsans", 40)


LETTER_WIDTH = 40
GAP = 15
letters = []
startx = round((WIDTH - (LETTER_WIDTH + GAP) * 13) / 2)
starty = 350
A = 65
for i in range(26):
    x = startx + ((LETTER_WIDTH + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + LETTER_WIDTH))
    letters.append([x, y, chr(A + i), True])

def draw():
    win.fill((255, 255, 255))

    for letter in letters:
        x, y, ltr, visible = letter
        text = LETTER_FONT.render(ltr, 1, BLACK)
        if letter[3]:
            win.blit(text, (x, y))

    pygame.display.update()


run = True

while run:

    draw()

    key = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key).upper()
        for letter in letters:
            if key == letter[2]:
                letter[3] = False


pygame.quit()
        