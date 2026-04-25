import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((255,255,255))

clock = pygame.time.Clock()

color = (255,0,0)
thickness = 5
mode = "rect"

drawing = False
start_pos = (0,0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # выбор инструментов
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = "rect"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_e:
                mode = "eraser"

            # выбор цвета
            elif event.key == pygame.K_1:
                color = (255,0,0)
            elif event.key == pygame.K_2:
                color = (0,255,0)
            elif event.key == pygame.K_3:
                color = (0,0,255)

        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            end_pos = event.pos
            drawing = False

            if mode == "rect":
                rect = pygame.Rect(start_pos, (end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]))
                pygame.draw.rect(screen, color, rect, thickness)

            elif mode == "circle":
                radius = int(((end_pos[0]-start_pos[0])**2 + (end_pos[1]-start_pos[1])**2)**0.5)
                pygame.draw.circle(screen, color, start_pos, radius, thickness)

        if event.type == pygame.MOUSEMOTION and drawing:
            if mode == "eraser":
                pygame.draw.circle(screen, (255,255,255), event.pos, 20)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
