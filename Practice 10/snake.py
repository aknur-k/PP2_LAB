import pygame
import random
import sys

pygame.init()


WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20  

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()


BLACK = (250, 250, 210)
GREEN = (0, 100, 0)
DARK_GREEN = (0, 255, 0)
RED = (225, 20, 60)
WHITE = (0, 0, 139)

font = pygame.font.SysFont("Arial", 24)

snake = [(100, 100), (80, 100), (60, 100)]  
direction = (CELL_SIZE, 0) 

score = 0
level = 1

speed = 8


def generate_food():
    """Generate food in random position not on snake or wall."""
    while True:
        x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        food = (x, y)

        
        if food not in snake:
            return food

food = generate_food()


def draw_info():
    text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(text, (10, 10))


running = True

while running:
    screen.fill(BLACK)

  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                direction = (0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                direction = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                direction = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                direction = (CELL_SIZE, 0)

    
    head_x, head_y = snake[0]
    dx, dy = direction

    new_head = (head_x + dx, head_y + dy)

  
    if (
        new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT
    ):
        print("Game Over: Hit wall")
        pygame.quit()
        sys.exit()


    if new_head in snake:
        print("Game Over: Hit self")
        pygame.quit()
        sys.exit()

   
    snake.insert(0, new_head)

   
    if new_head == food:
        score += 1
        food = generate_food()

        if score % 3 == 0:  
            level += 1
            speed += 2 

    else:
        snake.pop() 
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))

    
    for i, segment in enumerate(snake):
        color = GREEN if i == 0 else DARK_GREEN
        pygame.draw.rect(screen, color, (*segment, CELL_SIZE, CELL_SIZE))

   
    draw_info()

  
    pygame.display.update()

   
    clock.tick(speed)

pygame.quit()
