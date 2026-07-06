import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Two Rectangular Sprites")

player = pygame.Rect(100, 100, 60, 60)

enemy = pygame.Rect(500, 250, 60, 60)

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:

        player.y -= 1

    if keys[pygame.K_DOWN]:

        player.y += 1

    if keys[pygame.K_LEFT]:

        player.x -= 1

    if keys[pygame.K_RIGHT]:

        player.x += 1

    player.clamp_ip(screen.get_rect())

    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (255, 0, 0), player)   

    pygame.draw.rect(screen, (0, 0, 255), enemy)    

    pygame.display.flip()

pygame.quit()