import pygame
import random
import sys

pygame.init()

# -----------------------------
# SCREEN SETTINGS
# -----------------------------
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20  # size of snake block / food

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

# -----------------------------
# COLORS
# -----------------------------
BLACK = (250, 250, 210)
GREEN = (255, 105, 180)
DARK_GREEN = (255, 120, 190)
RED = (225, 20, 60)
WHITE = (0, 0, 139)

font = pygame.font.SysFont("Arial", 24)

# -----------------------------
# INITIAL GAME STATE
# -----------------------------
snake = [(100, 100), (80, 100), (60, 100)]  # initial snake body
direction = (CELL_SIZE, 0)  # moving right

score = 0
level = 1

# speed increases with level
speed = 8

# -----------------------------
# FUNCTION: GENERATE FOOD
# -----------------------------
def generate_food():
    """Generate food in random position not on snake or wall."""
    while True:
        x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        food = (x, y)

        # ensure food is not inside snake
        if food not in snake:
            return food

food = generate_food()

# -----------------------------
# FUNCTION: DRAW TEXT
# -----------------------------
def draw_info():
    text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(text, (10, 10))

# -----------------------------
# GAME LOOP
# -----------------------------
running = True

while running:
    screen.fill(BLACK)

    # -------------------------
    # EVENT HANDLING
    # -------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # control snake direction
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                direction = (0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                direction = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                direction = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                direction = (CELL_SIZE, 0)

    # -------------------------
    # MOVE SNAKE
    # -------------------------
    head_x, head_y = snake[0]
    dx, dy = direction

    new_head = (head_x + dx, head_y + dy)

    # -------------------------
    # WALL COLLISION CHECK
    # -------------------------
    if (
        new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT
    ):
        print("Game Over: Hit wall")
        pygame.quit()
        sys.exit()

    # -------------------------
    # SELF COLLISION CHECK
    # -------------------------
    if new_head in snake:
        print("Game Over: Hit self")
        pygame.quit()
        sys.exit()

    # add new head
    snake.insert(0, new_head)

    # -------------------------
    # FOOD COLLISION
    # -------------------------
    if new_head == food:
        score += 1
        food = generate_food()

        # ---------------------
        # LEVEL SYSTEM
        # ---------------------
        if score % 3 == 0:  # every 3 foods → level up
            level += 1
            speed += 2  # increase speed

    else:
        snake.pop()  # remove tail if no food eaten

    # -------------------------
    # DRAW FOOD
    # -------------------------
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))

    # -------------------------
    # DRAW SNAKE
    # -------------------------
    for i, segment in enumerate(snake):
        color = GREEN if i == 0 else DARK_GREEN
        pygame.draw.rect(screen, color, (*segment, CELL_SIZE, CELL_SIZE))

    # -------------------------
    # DRAW SCORE & LEVEL
    # -------------------------
    draw_info()

    # -------------------------
    # UPDATE SCREEN
    # -------------------------
    pygame.display.update()

    # control speed
    clock.tick(speed)

pygame.quit()
