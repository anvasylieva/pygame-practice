import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)

run = True
while run:
    pygame.draw.rect(screen, 'red', [200, 200, 100, 100])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()
