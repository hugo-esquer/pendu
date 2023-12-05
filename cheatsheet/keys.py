import pygame

pygame.init()
win = pygame.display.set_mode((900, 500))

FPS = 60
clock = pygame.time.Clock()
run = True

while run:
    clock.tick(FPS)
    win.fill((255, 255, 255))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)
            print(key.upper())

pygame.quit()