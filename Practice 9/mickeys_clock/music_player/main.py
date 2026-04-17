import pygame
from player import MusicPlayer

pygame.init()

WIDTH, HEIGHT = 700, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🎧 Music Player")

font = pygame.font.SysFont("Arial", 26)

player = MusicPlayer("music")

running = True
while running:
    screen.fill((20, 20, 20))

    # 🎵 текст
    track = font.render(
        f"Track: {player.current_track()}",
        True,
        (255, 182, 193)
    )
    screen.blit(track, (20, 40))

    controls = font.render(
        "P=Play  Space=Pause  S=Stop  N=Next  B=Back  Q=Quit",
        True,
        (200, 200, 200)
    )
    screen.blit(controls, (20, 80))

    # 🎚️ ПРОГРЕСС-БАР
    progress = player.get_progress()
    bar_x, bar_y = 20, 150
    bar_width, bar_height = 600, 20

    pygame.draw.rect(screen, (50, 50, 50),
                     (bar_x, bar_y, bar_width, bar_height))

    fill_width = min(progress * 10, bar_width)  # скорость заполнения
    pygame.draw.rect(screen, (255, 105, 180),
                     (bar_x, bar_y, fill_width, bar_height))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_q:
                running = False

            elif event.key == pygame.K_p:
                player.play()

            elif event.key == pygame.K_SPACE:
                player.pause()

            elif event.key == pygame.K_s:
                player.stop()

            elif event.key == pygame.K_n:
                player.next()

            elif event.key == pygame.K_b:
                player.prev()

pygame.quit()
