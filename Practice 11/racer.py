import pygame
import random
import time
import os

pygame.init()

# -------------------- SETTINGS --------------------
WIDTH = 400
HEIGHT = 600
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

clock = pygame.time.Clock()

BASE_DIR = os.path.dirname(__file__)
RESOURCES = os.path.join(BASE_DIR, "resources")

# -------------------- LOAD IMAGES --------------------
background = pygame.image.load(os.path.join(RESOURCES, "AnimatedStreet.png"))
player_img = pygame.image.load(os.path.join(RESOURCES, "Player.png"))
enemy_img = pygame.image.load(os.path.join(RESOURCES, "Enemy.png"))
coin_img = pygame.image.load(os.path.join(RESOURCES, "coinnn.png"))

player_img = pygame.transform.scale(player_img, (50, 90))
enemy_img = pygame.transform.scale(enemy_img, (50, 90))
coin_img = pygame.transform.scale(coin_img, (40, 40))

# -------------------- SOUND --------------------
try:
    pygame.mixer.music.load(os.path.join(RESOURCES, "background.wav"))
    pygame.mixer.music.play(-1)

    crash_sound = pygame.mixer.Sound(os.path.join(RESOURCES, "crash.wav"))
except:
    crash_sound = None

# -------------------- FONTS --------------------
font = pygame.font.SysFont("Verdana", 20)
big_font = pygame.font.SysFont("Verdana", 50)

# -------------------- GAME VARIABLES --------------------
score = 0
coins_collected = 0
enemy_speed = 6  # базовая скорость врага
coin_speed = 5

# -------------------- PLAYER --------------------
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 70))

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-6, 0)

        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.move_ip(6, 0)

# -------------------- ENEMY --------------------
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect(
            center=(random.randint(50, WIDTH - 50), -100)
        )

    def move(self):
        global score
        self.rect.move_ip(0, enemy_speed)

        # если враг ушел вниз → увеличиваем score
        if self.rect.top > HEIGHT:
            score += 1
            self.rect.center = (random.randint(50, WIDTH - 50), -100)

# -------------------- COIN WITH WEIGHT --------------------
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_img
        self.reset()

    def reset(self):
        # случайная позиция
        self.rect = self.image.get_rect(
            center=(random.randint(30, WIDTH - 30), random.randint(-500, -50))
        )

        # случайный вес монеты
        self.weight = random.choice([1, 2, 3])

    def move(self):
        self.rect.move_ip(0, coin_speed)

        # если вышла за экран → новая монета
        if self.rect.top > HEIGHT:
            self.reset()

    def draw(self):
        # цвет зависит от веса
        if self.weight == 1:
            tint = (255, 255, 0)   # желтый
        elif self.weight == 2:
            tint = (0, 255, 0)     # зеленый
        else:
            tint = (255, 0, 0)     # красный

        # окрашиваем копию изображения
        img = self.image.copy()
        img.fill(tint, special_flags=pygame.BLEND_MULT)

        screen.blit(img, self.rect)

# -------------------- INIT --------------------
player = Player()
enemy = Enemy()

coins = pygame.sprite.Group()
for _ in range(3):
    coins.add(Coin())

enemies = pygame.sprite.Group()
enemies.add(enemy)

running = True

# -------------------- MAIN LOOP --------------------
while running:
    screen.blit(background, (0, 0))

    # -------- EVENTS --------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # -------- MOVEMENT --------
    player.move()
    enemy.move()

    for coin in coins:
        coin.move()

    # -------- COLLECT COINS --------
    collected = pygame.sprite.spritecollide(player, coins, False)
    for coin in collected:
        coins_collected += coin.weight   # учитываем вес
        coin.reset()

        # увеличение скорости каждые 5 монет
        if coins_collected % 5 == 0:
            enemy_speed += 1

    # -------- COLLISION --------
    if pygame.sprite.spritecollideany(player, enemies):
        if crash_sound:
            crash_sound.play()

        screen.fill((255, 0, 0))
        game_over = big_font.render("GAME OVER", True, (0, 0, 0))
        screen.blit(game_over, (60, HEIGHT // 2))
        pygame.display.update()
        time.sleep(2)
        running = False

    # -------- DRAW --------
    screen.blit(enemy.image, enemy.rect)
    screen.blit(player.image, player.rect)

    for coin in coins:
        coin.draw()

    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    coin_text = font.render(f"Coins: {coins_collected}", True, (0, 0, 0))

    screen.blit(score_text, (10, 10))
    screen.blit(coin_text, (260, 10))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
