import pygame

pygame.init()

screen= pygame.display.set_mode((800,800))

done=False

while not done:

    for event in pygame.event.get():

        if event.type== pygame.QUIT:

            done=True

    pygame.draw.rect(screen , (0,125,125), pygame.Rect(175,200,450,300))

    pygame.display.flip()