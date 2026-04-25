import pygame
import sys

pygame.init()

# -------------------------
# SCREEN SETTINGS
# -------------------------
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint App")

clock = pygame.time.Clock()

# -------------------------
# COLORS
# -------------------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

colors = [BLACK, RED, GREEN, BLUE, YELLOW]
color_names = ["BLACK", "RED", "GREEN", "BLUE", "YELLOW"]

current_color = BLACK
brush_size = 5

# -------------------------
# CANVAS
# -------------------------
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(WHITE)

# -------------------------
# MODES
# -------------------------
mode = "brush"   # brush | rect | circle | eraser

start_pos = None  # for shapes

# -------------------------
# DRAW UI TEXT
# -------------------------
font = pygame.font.SysFont("Arial", 20)

def draw_ui():
    text = font.render(
        f"Mode: {mode} | Color: {color_names[colors.index(current_color)]} | (B=Brush R=Rect C=Circle E=Eraser)",
        True, (0, 0, 0)
    )
    screen.blit(text, (10, 10))

# -------------------------
# MAIN LOOP
# -------------------------
running = True

while running:
    screen.fill(WHITE)
    screen.blit(canvas, (0, 0))

    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    # -------------------------
    # EVENTS
    # -------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # KEY CONTROLS
        elif event.type == pygame.KEYDOWN:

            # TOOL SELECTION
            if event.key == pygame.K_b:
                mode = "brush"
            elif event.key == pygame.K_r:
                mode = "rect"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_e:
                mode = "eraser"

            # COLOR SELECTION (number keys)
            elif event.key == pygame.K_1:
                current_color = BLACK
            elif event.key == pygame.K_2:
                current_color = RED
            elif event.key == pygame.K_3:
                current_color = GREEN
            elif event.key == pygame.K_4:
                current_color = BLUE
            elif event.key == pygame.K_5:
                current_color = YELLOW

        # START SHAPE
        elif event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = event.pos

        # END SHAPE
        elif event.type == pygame.MOUSEBUTTONUP:
            if start_pos:
                end_pos = event.pos

                # -------------------------
                # RECTANGLE TOOL
                # -------------------------
                if mode == "rect":
                    x = min(start_pos[0], end_pos[0])
                    y = min(start_pos[1], end_pos[1])
                    w = abs(start_pos[0] - end_pos[0])
                    h = abs(start_pos[1] - end_pos[1])

                    pygame.draw.rect(canvas, current_color, (x, y, w, h), 2)

                # -------------------------
                # CIRCLE TOOL
                # -------------------------
                elif mode == "circle":
                    radius = int(((end_pos[0] - start_pos[0]) ** 2 +
                                  (end_pos[1] - start_pos[1]) ** 2) ** 0.5)

                    pygame.draw.circle(canvas, current_color, start_pos, radius, 2)

                start_pos = None

    # -------------------------
    # BRUSH / ERASER DRAWING
    # -------------------------
    if pygame.mouse.get_pressed()[0]:

        if mode == "brush":
            pygame.draw.circle(canvas, current_color, (mouse_x, mouse_y), brush_size)

        elif mode == "eraser":
            pygame.draw.circle(canvas, WHITE, (mouse_x, mouse_y), brush_size * 2)

    # -------------------------
    # DRAW UI
    # -------------------------
    draw_ui()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
