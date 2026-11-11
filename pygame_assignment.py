import pygame
pygame.init()

pygame.display.set_caption ("MY FIRST GAME WINDOW")
screen = pygame.display.set_mode((800,600))
player_image = pygame.image.load("penguin.png")
done = False
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            done = True 

    img = player_image.get_rect(center = (300,400))

    screen.blit(player_image,img)
    pygame.display.flip()
