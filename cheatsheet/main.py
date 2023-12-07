import pygame
import random
import pygame_menu
from pygame_menu import themes

# setup display
pygame.init()
WIDTH, HEIGHT = 900, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu du Pendu")

# color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# font
LETTER_FONT = pygame.font.SysFont("lucidaconsole", 40)
SCORE_FONT = pygame.font.SysFont("lucidaconsole", 20)

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
score = 0
name = ""

def reset():
    global hangman_statuts
    global word
    global guessed

    hangman_statuts = 0
    word = None
    guessed = []
    word = random_word("mots.txt")
    for i in range(26):
        x = startx + ((LETTER_WIDTH + GAP) * (i % 13))
        y = starty + ((i // 13) * (GAP + LETTER_WIDTH))
        letters.append([x, y, chr(A + i), True])

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
    win.blit(images[hangman_statuts], (400, 5))

    #draw Word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = LETTER_FONT.render(display_word, 1, BLACK)
    win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2))

    #draw score
    text = SCORE_FONT.render(f"{name} score : {score}", 1, BLACK)
    win.blit(text, (20, 20))

    pygame.display.update()

def display_win_loose(message):
    pygame.time.delay(500)
    win.fill(WHITE)
    text = LETTER_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH / 2 - text.get_width()/2, HEIGHT / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(3000)


def main_game():
    global hangman_statuts, score
    FPS = 60
    run = True

    while run:
        clock.tick(FPS)

        key = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    reset()
                    return
            
            if event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key).upper()
                if key not in guessed:
                    guessed.append(key)
                    if key not in word:
                            hangman_statuts +=1
            for letter in letters:
                if key == letter[2]:
                    letter[3] = False

        draw()

        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break

        if won:
            display_win_loose("Bravo, tu as trouvé!")
            score +=1
            reset()
        
        if hangman_statuts == 6:
            display_win_loose("Dommage")
            reset()
            score = 0
            break
def get_name(player_name):
    global name
    name = player_name

def add_word(word):
    with open('mots.txt', "a") as f:
        f.write("\n" + word.upper())
    text = LETTER_FONT.render(f"{word} a été ajouté", 1, BLACK)
    win.blit(text, (WIDTH / 2 - text.get_width()/2, (HEIGHT / 3) * 2 - text.get_height() / 2))
    pygame.display.update()
    new_word.clear()
    new_word.add.text_input("nouveau mot : ", default="", onreturn = add_word)
    pygame.time.delay(1500)
    
def set_difficulty(value, difficulty):
    print(value)
    print(difficulty)

def new_word_menu():
    mainmenu._open(new_word)

def level_menu():
    mainmenu._open(level)

mainmenu = pygame_menu.Menu("Bienvenue", WIDTH, HEIGHT, theme=themes.THEME_BLUE)
mainmenu.add.text_input("Nom: ", default="Prenom", maxchar=20, repeat_keys = False, onchange= get_name)
mainmenu.add.button("Jouer", main_game)
mainmenu.add.button("Ajouter un mot", new_word_menu)
mainmenu.add.button("Difficulté", level_menu)
mainmenu.add.button("Quitter", pygame_menu.events.EXIT)

level = pygame_menu.Menu("Choix de la difficulté", WIDTH, HEIGHT, theme=themes.THEME_BLUE)
level.add.selector("Difficulté: ", [("Difficile", 1), ("Moyen", 2), ("Facile", 3)], onchange=set_difficulty)

new_word = pygame_menu.Menu("Ajouter un mot: ", WIDTH, HEIGHT, theme=themes.THEME_BLUE)
new_word.add.text_input("nouveau mot : ", default="", onreturn = add_word)


running = True
while running:
    clock = pygame.time.Clock()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if mainmenu.is_enabled():
            mainmenu.mainloop(win)
        
        pygame.display.update()
        clock.tick(60)

pygame.quit()