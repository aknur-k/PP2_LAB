import pygame, random

pygame.init()

WIDTH, HEIGHT = 600, 600
CELL = 30

screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont("Verdana", 20)
big_font = pygame.font.SysFont("Verdana", 40)

WHITE = (255, 255, 255)
GREEN = (255, 0, 0)
RED = (200, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (20, 20, 20)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.body = [Point(5, 5), Point(4, 5), Point(3, 5)]
        self.dx = 1
        self.dy = 0
        self.grow = False

    def move(self):
        new_head = Point(self.body[0].x + self.dx, self.body[0].y + self.dy)
        self.body.insert(0, new_head)

        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def change_dir(self, dx, dy):
        if len(self.body) > 1:
            if dx == -self.dx and dy == -self.dy:
                return
        self.dx = dx
        self.dy = dy

    def draw(self):
        for i, segment in enumerate(self.body):
            color = RED if i == 0 else YELLOW
            pygame.draw.rect(screen, color, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def collide_self(self):
        return any(seg.x == self.body[0].x and seg.y == self.body[0].y for seg in self.body[1:])

    def collide_wall(self):
        head = self.body[0]
        return head.x < 0 or head.x >= WIDTH // CELL or head.y < 0 or head.y >= HEIGHT // CELL

    def eat(self, food):
        if self.body[0].x == food.x and self.body[0].y == food.y:
            self.grow = True
            return True
        return False

class Food:
    def __init__(self, snake):
        self.generate(snake)

    def generate(self, snake):
        while True:
            self.x = random.randint(0, WIDTH // CELL - 1)
            self.y = random.randint(0, HEIGHT // CELL - 1)

            if all(seg.x != self.x or seg.y != self.y for seg in snake.body):
                break

    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.x * CELL, self.y * CELL, CELL, CELL))

def show_game_over(score):
    screen.fill(BLACK)
    text = big_font.render("GAME OVER", True, RED)
    score_text = font.render(f"Score: {score}", True, WHITE)

    screen.blit(text, (WIDTH//2 - 120, HEIGHT//2 - 50))
    screen.blit(score_text, (WIDTH//2 - 50, HEIGHT//2 + 10))
    pygame.display.update()
    pygame.time.delay(2000)

snake = Snake()
food = Food(snake)

score = 0
level = 1
FPS = 15

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.change_dir(1, 0)
            elif event.key == pygame.K_LEFT:
                snake.change_dir(-1, 0)
            elif event.key == pygame.K_UP:
                snake.change_dir(0, -1)
            elif event.key == pygame.K_DOWN:
                snake.change_dir(0, 1)

    snake.move()

    if snake.eat(food):
        score += 1
        food.generate(snake)

        if score % 3 == 0:
            level += 1
            if level <= 3:
                FPS += 2
            else:
                FPS += 3

    if snake.collide_wall() or snake.collide_self():
        show_game_over(score)
        running = False

    screen.fill(BLACK)
    snake.draw()
    food.draw()

    screen.blit(font.render(f"Score: {score}", True, WHITE), (10, 10))
    screen.blit(font.render(f"Level: {level}", True, WHITE), (10, 35))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
