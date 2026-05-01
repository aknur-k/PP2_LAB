import pygame, random

pygame.init()

WIDTH = 600
HEIGHT = 600
CELL = 30

screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont("Verdana", 20)

WHITE = (0, 0, 139)
GREEN = (255, 120, 190)
RED = (0, 100, 0)
YELLOW = (0, 255, 0)
BLACK = (250, 250, 210)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

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
        pygame.draw.rect(screen, RED, (self.body[0].x*CELL, self.body[0].y*CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, YELLOW, (segment.x*CELL, segment.y*CELL, CELL, CELL))

    def collide_food(self, food):
        if self.body[0].x == food.x and self.body[0].y == food.y:
            self.body.append(Point(self.body[-1].x, self.body[-1].y))
            return True
        return False

    def collide_wall(self):
        return self.body[0].x < 0 or self.body[0].x >= WIDTH//CELL or self.body[0].y < 0 or self.body[0].y >= HEIGHT//CELL

class Food:
    def __init__(self, snake):
        self.generate(snake)

    def generate(self, snake):
        while True:
            self.x = random.randint(0, WIDTH//CELL-1)
            self.y = random.randint(0, HEIGHT//CELL-1)

            on_snake = False
            for segment in snake.body:
                if segment.x == self.x and segment.y == self.y:
                    on_snake = True

            if not on_snake:
                break

    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.x*CELL, self.y*CELL, CELL, CELL))

snake = Snake()
food = Food(snake)

score = 0
level = 1
FPS = 5

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

    snake.move()

    # если съел еду
    if snake.collide_food(food):
        score += 1
        food.generate(snake)

        # каждые 3 очка новый уровень
        if score % 3 == 0:
            level += 1
            FPS += 2

    # столкновение со стеной
    if snake.collide_wall():
        running = False

    screen.fill(BLACK)
    snake.draw()
    food.draw()

    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)

    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 35))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
