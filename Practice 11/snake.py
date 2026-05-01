import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 600
CELL = 30

screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont("Verdana", 20)

WHITE = (255,255,255)
GREEN = (0,255,0)
YELLOW = (255,255,0)
RED = (255,0,0)
BLACK = (0,0,0)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# ---------------- SNAKE ----------------
class Snake:
    def __init__(self):
        self.body = [Point(5,5), Point(4,5), Point(3,5)]
        self.dx = 1
        self.dy = 0

    def move(self):
        for i in range(len(self.body)-1, 0, -1):
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment.x*CELL, segment.y*CELL, CELL, CELL))

# ---------------- FOOD ----------------
class Food:
    def __init__(self, snake):
        self.generate(snake)

    def generate(self, snake):
        while True:
            self.x = random.randint(0, WIDTH//CELL - 1)
            self.y = random.randint(0, HEIGHT//CELL - 1)
            self.weight = random.choice([1, 2, 3])
            self.spawn_time = pygame.time.get_ticks()

            if all(seg.x != self.x or seg.y != self.y for seg in snake.body):
                break

    def draw(self):
        if self.weight == 1:
            color = GREEN
        elif self.weight == 2:
            color = YELLOW
        else:
            color = RED

        pygame.draw.rect(screen, color, (self.x*CELL, self.y*CELL, CELL, CELL))

snake = Snake()
food = Food(snake)

score = 0
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.dx, snake.dy = 1, 0
            elif event.key == pygame.K_LEFT:
                snake.dx, snake.dy = -1, 0
            elif event.key == pygame.K_UP:
                snake.dx, snake.dy = 0, -1
            elif event.key == pygame.K_DOWN:
                snake.dx, snake.dy = 0, 1
    def show_game_over(score):
        screen.fill(BLACK)
        text = font.render("GAME OVER", True, RED)
        score_text = font.render(f"Score: {score}", True, WHITE)

        screen.blit(text, (WIDTH//2 - 80, HEIGHT//2 - 20))
        screen.blit(score_text, (WIDTH//2 - 60, HEIGHT//2 + 20))

        pygame.display.update()
        pygame.time.delay(2000)

    snake.move()

    head = snake.body[0]

    if head.x < 0 or head.x >= WIDTH // CELL or head.y < 0 or head.y >= HEIGHT // CELL:
        show_game_over(score)
        running = False


    # food collision
    if snake.body[0].x == food.x and snake.body[0].y == food.y:
        score += food.weight

        for _ in range(food.weight):
            snake.body.append(Point(snake.body[-1].x, snake.body[-1].y))

        food.generate(snake)

    # food disappears after 5 seconds
    if pygame.time.get_ticks() - food.spawn_time > 5000:
        food.generate(snake)

    screen.fill(BLACK)
    snake.draw()
    food.draw()

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10,10))

    pygame.display.update()
    clock.tick(5)

pygame.quit()
