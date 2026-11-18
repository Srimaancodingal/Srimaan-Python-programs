
import pygame
import random

pygame.init()

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Collision Color Game")

sp1 = pygame.Rect(200, 200, 50, 50)
sp2 = pygame.Rect(50, 50, 50, 50)

color1 = (0, 0, 225)
color2 = (0, 225, 0)

running = True
collided = False

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                sp1.x += 20
            elif event.key == pygame.K_LEFT:
                sp1.x -= 20
            elif event.key == pygame.K_DOWN:
                sp1.y += 20
            elif event.key == pygame.K_UP:
                sp1.y -= 20

    if sp1.colliderect(sp2):
        if not collided:
            print("TIME TO CHNAGE COLOURS!!!!!!")

            color1 = (random.randint(0, 225),
                      random.randint(0, 225),
                      random.randint(0, 225))

            color2 = (random.randint(0, 225),
                      random.randint(0, 225),
                      random.randint(0, 225))

        collided = True
    else:
        collided = False

    screen.fill((225, 225, 225))

    pygame.draw.rect(screen, color1, sp1)
    pygame.draw.rect(screen, color2, sp2)

    pygame.display.flip()

pygame.quit()
