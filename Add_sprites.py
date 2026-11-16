import pygame 
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("My first game")
player = pygame.Rect(100, 100, 50, 50)
enemy = pygame.Rect(400,300,50,50)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit ()
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen,(225, 0, 0), player)
    pygame.draw.rect(screen,(0, 0, 225), enemy)
    pygame.display.flip()
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_RIGHT]:
        player.x += 2

    elif keys[pygame.K_LEFT]:
        player.x -= 2

    elif keys[pygame.K_DOWN]:
        player.y += 2

    elif keys[pygame.K_UP]:
        player.y -= 2
    
        if player.left < 0:
            player.left = 0

        if player.right > 500:
            player.right = 500

        if player.top < 0:
            player.top = 0

        if player.bottom > 500:
            player.bottom = 500
        
        if player.colliderect(enemy):
            print ("You've hit the enemy")
        pygame.display.update()
        pygame.display.flip()
    