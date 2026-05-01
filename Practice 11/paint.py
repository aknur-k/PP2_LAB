import pygame
import math

pygame.init()

# -------------------- SCREEN --------------------
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSIS Paint")

clock = pygame.time.Clock()
screen.fill((255, 255, 255))

# -------------------- SETTINGS --------------------
color = (255, 0, 0)
thickness = 3
mode = "rect"

drawing = False
start_pos = (0, 0)

# -------------------- SHAPES FUNCTIONS --------------------
def draw_square(s, e):
    size = min(abs(e[0]-s[0]), abs(e[1]-s[1]))
    rect = pygame.Rect(s[0], s[1], size, size)
    pygame.draw.rect(screen, color, rect, thickness)


def draw_right_triangle(s, e):
    points = [s, (s[0], e[1]), e]
    pygame.draw.polygon(screen, color, points, thickness)


def draw_equilateral_triangle(s, e):
    x1, y1 = s
    x2, y2 = e
    height = abs(y2 - y1)

    points = [
        (x1, y1),
        (x2, y1),
        ((x1 + x2)//2, y1 - height)
    ]
    pygame.draw.polygon(screen, color, points, thickness)


def draw_rhombus(s, e):
    cx = (s[0] + e[0]) // 2
    cy = (s[1] + e[1]) // 2

    dx = abs(e[0] - s[0]) // 2
    dy = abs(e[1] - s[1]) // 2

    points = [
        (cx, cy - dy),
        (cx + dx, cy),
        (cx, cy + dy),
        (cx - dx, cy)
    ]
    pygame.draw.polygon(screen, color, points, thickness)


def draw_circle(s, e):
    radius = int(math.hypot(e[0]-s[0], e[1]-s[1]))
    pygame.draw.circle(screen, color, s, radius, thickness)

# -------------------- MAIN LOOP --------------------
running = True
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # -------- KEYBOARD --------
        if event.type == pygame.KEYDOWN:

            # tools
            if event.key == pygame.K_r:
                mode = "rect"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_s:
                mode = "square"
            elif event.key == pygame.K_t:
                mode = "right_triangle"
            elif event.key == pygame.K_f:
                mode = "equilateral_triangle"
            elif event.key == pygame.K_d:
                mode = "rhombus"
            elif event.key == pygame.K_e:
                mode = "eraser"

            # colors
            elif event.key == pygame.K_1:
                color = (255, 0, 0)
            elif event.key == pygame.K_2:
                color = (0, 255, 0)
            elif event.key == pygame.K_3:
                color = (0, 0, 255)
            elif event.key == pygame.K_4:
                color = (255, 255, 255)

        # -------- MOUSE DOWN --------
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

        # -------- MOUSE UP --------
        if event.type == pygame.MOUSEBUTTONUP:
            end_pos = event.pos
            drawing = False

            # -------- SHAPES FINAL DRAW --------
            if mode == "rect":
                pygame.draw.rect(screen, color,
                                 pygame.Rect(start_pos, (end_pos[0]-start_pos[0], end_pos[1]-start_pos[1])),
                                 thickness)

            elif mode == "circle":
                draw_circle(start_pos, end_pos)

            elif mode == "square":
                draw_square(start_pos, end_pos)

            elif mode == "right_triangle":
                draw_right_triangle(start_pos, end_pos)

            elif mode == "equilateral_triangle":
                draw_equilateral_triangle(start_pos, end_pos)

            elif mode == "rhombus":
                draw_rhombus(start_pos, end_pos)

        # -------- ERASER (drag) --------
        if event.type == pygame.MOUSEMOTION and drawing:
            if mode == "eraser":
                pygame.draw.circle(screen, (0, 0, 0), event.pos, 20)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
