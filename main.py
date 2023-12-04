import pygame
import pygame_menu
from pygame_menu import themes

pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 500
GRAY = (229, 231, 246)
clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Menu principal")

def start_the_game():
    pass

def add_word():
    pass


mainmenu = pygame_menu.Menu("Bienvenue", SCREEN_WIDTH, SCREEN_HEIGHT, theme=themes.THEME_BLUE)
mainmenu.add.text_input("Nom: ", default="Prenom", maxchar=20, repeat_keys = False)
mainmenu.add.button("Jouer", start_the_game)
mainmenu.add.button("Ajouter un mot", add_word)
mainmenu.add.button("Difficulté")
mainmenu.add.button("Quitter", pygame_menu.events.EXIT)

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        
        screen.fill(GRAY)

        if mainmenu.is_enabled():
            mainmenu.mainloop(screen)
        
        pygame.display.update()
        clock.tick(60)


pygame.quit()