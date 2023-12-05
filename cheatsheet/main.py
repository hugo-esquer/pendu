import pygame
import random

# setup display
pygame.init()
WIDTH, HEIGHT = 900, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu du Pendu")

# color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# font
LETTER_FONT = pygame.font.SysFont("comicsans", 40)

# load letter
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

# load images
images = []
for i in range(7):
    image = pygame.image.load(f"hangman{i}.png")
    images.append(image)

# random word
def random_word(file):
    with open(file, "r") as f:
        line = f.readlines()
        random_line = random.choice(line).strip().upper()
        return random_line

# game variable
hangman_statuts = 0
word = random_word("mots.txt")
guessed = []

# setup game loop
FPS = 60
clock = pygame.time.Clock()
run = True

# fonctions
def draw():
    win.fill(WHITE)

    # draw letters
    for letter in letters:
        x, y, ltr, visible = letter
        text = LETTER_FONT.render(ltr, 1, BLACK)
        if visible:
            win.blit(text, (x, y))

    # draw images
    win.blit(images[hangman_statuts], (150, 100))

    #draw Word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = LETTER_FONT.render(display_word, 1, BLACK)
    win.blit(text, (450, 150))

    pygame.display.update()


while run:
    clock.tick(FPS)

    draw()

    key = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key).upper()
            guessed += [key]
            if key not in word:
                hangman_statuts +=1
        for letter in letters:
            if key == letter[2]:
                letter[3] = False

    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break

    if won:
        print("won")
        break
    
    if hangman_statuts == 6:
        print("loose!")
        break

pygame.quit()