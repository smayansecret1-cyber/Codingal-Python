import pygame

import random

pygame.init()

screen = pygame.display.set_mode((800, 800))

pygame.display.set_caption("Two Sprites with Custom Event")

class Box(pygame.sprite.Sprite):

    def __init__(self, color, x, y):

        super().__init__()

        self.image = pygame.Surface((100, 100))

        self.image.fill(color)

        self.rect = self.image.get_rect()

        self.rect.x = x

        self.rect.y = y

sprite1 = Box((255, 0, 0), 150, 250)

sprite2 = Box((0, 0, 255), 450, 250)

all_sprites = pygame.sprite.Group()

all_sprites.add(sprite1)

all_sprites.add(sprite2)

CHANGE_COLOR = pygame.USEREVENT + 1

pygame.time.set_timer(CHANGE_COLOR, 2000)

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        if event.type == CHANGE_COLOR:

            color1 = (
                random.randint(0, 255),

                random.randint(0, 255),

                random.randint(0, 255)
            )

            color2 = (
                random.randint(0, 255),

                random.randint(0, 255),

                random.randint(0, 255)
            )

            sprite1.image.fill(color1)

            sprite2.image.fill(color2)

    screen.fill((255, 255, 255))

    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()