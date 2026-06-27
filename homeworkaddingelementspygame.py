import pygame
import sys

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Adding image')

try:
    penguin_image = pygame.transform.scale(
        pygame.image.load('ahem.jpg').convert_alpha(),
        (300,300)
    )
except FileNotFoundError as e:
    print(f"Error loading image: {e}")
    pygame.quit()
    sys.exit()

penguin_rect = penguin_image.get_rect(
    center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30)
)

font = pygame.font.Font(None, 36)

text = font.render('My first game screen', True, pygame.Color('black'))

text_rect = text.get_rect(
    center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110)
)

def game_loop():
    clock = pygame.time.Clock()
    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Gray background
        display_surface.fill((50, 50, 50))

        # Draw image
        display_surface.blit(penguin_image, penguin_rect)

        # Draw text
        display_surface.blit(text, text_rect)

        pygame.display.flip()

        clock.tick(30)

    pygame.draw.rect((0,125,125), pygame.Rect(175,200,450,300))

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    game_loop()