import pygame

# setup display
pygame.init()
WIDTH, HEIGHT = 900, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu du Pendu")

# color
WHITE = (255, 255, 255)

# load images
images = []
for i in range(7):
    image = pygame.image.load(f"hangman{i}.png")
    images.append(image)

# game variable
hangman_statuts = 0

# setup game loop
FPS = 60
clock = pygame.time.Clock()
run = True

def draw():
    win.fill(WHITE)

    # draw letters
    

    win.blit(images[hangman_statuts], (150, 100))
    pygame.display.update()


while run:
    clock.tick(FPS)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False




pygame.quit()