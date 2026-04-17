import pygame
from clock import Clock

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

import os

BASE_DIR = os.path.dirname(__file__)
background_path = os.path.join(BASE_DIR, "images", "mickey_clocks.png")

background = pygame.image.load(background_path)

background = pygame.transform.scale(background, (WIDTH, HEIGHT))

clock = pygame.time.Clock()
mickey = Clock(screen)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    mickey.update()

    pygame.display.update()
    clock.tick(1)

pygame.quit()
