import pygame
import random

pygame.init()
pygame.mixer.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Collision")

background = pygame.image.load("map.png").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

pygame.mixer.music.load("Pacman-fever.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

player_image = pygame.image.load("player.png").convert_alpha()
player_image = pygame.transform.scale(player_image, (80, 100))

player = player_image.get_rect()
player.x = WIDTH // 2
player.y = HEIGHT - 120

enemy_image = pygame.image.load("enymy.png").convert_alpha()
enemy_image = pygame.transform.scale(enemy_image, (70, 50))

enemies = []

for i in range(7):

    enemy = enemy_image.get_rect()

    enemy.x = random.randint(0, WIDTH - enemy.width)
    enemy.y = random.randint(0, HEIGHT - enemy.height - 120)

    enemies.append(enemy)

score = 0

font = pygame.font.SysFont("Arial", 35)

clock = pygame.time.Clock()

running = True

while running:

    clock.tick(60)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= 5

    if keys[pygame.K_RIGHT]:
        player.x += 5

    if keys[pygame.K_UP]:
        player.y -= 5

    if keys[pygame.K_DOWN]:
        player.y += 5

    player.clamp_ip(screen.get_rect())

    for enemy in enemies:

        if player.colliderect(enemy):

            score += 1

            enemy.x = random.randint(0, WIDTH - enemy.width)
            enemy.y = random.randint(0, HEIGHT - enemy.height - 120)

    screen.blit(background, (0, 0))

    for enemy in enemies:
        screen.blit(enemy_image, enemy)

    screen.blit(player_image, player)

    score_text = font.render("Score : " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.mixer.music.stop()
pygame.quit()