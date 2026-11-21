
import pygame, random

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

text = pygame.font.SysFont("Arial", 50)

game_over = False
running = True

player = pygame.Rect(200, 500, 50, 50)
enemy = pygame.Rect(400, 500, 50, 50)

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player.x -= 5

        if keys[pygame.K_RIGHT]:
            player.x += 5

        if player.colliderect(enemy):
            game_over = True

    screen.fill((225, 225, 225))

    if game_over:
        message = text.render("YOU WIN!!!", True, (0, 0, 0))
        screen.blit(message, (100, 350))

    else:
        pygame.draw.rect(screen, (0, 0, 225), player)
        pygame.draw.rect(screen, (255, 0, 0), enemy)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
