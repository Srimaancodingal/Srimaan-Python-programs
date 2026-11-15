
import pygame

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hi Codingal")
done = False
clock = pygame.time.Clock()
while not done:
    display_surface.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.draw.rect(display_surface, (0, 225, 125), (200, 200, 100, 100))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

