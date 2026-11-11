import pygame
pygame.init()

screen = pygame.display.set_mode  ((300,300))

done = False 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.draw.rect(screen,(0,225,125), pygame.Rect(30,60,30,60))
    pygame.display.flip()