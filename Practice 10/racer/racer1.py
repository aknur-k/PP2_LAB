import pygame
import random
import time
import os

pygame.init()

# ---------------- SETTINGS ----------------
WIDTH = 400
HEIGHT = 600
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

clock = pygame.time.Clock()

# ---------------- FILE PATHS ----------------
BASE_DIR = os.path.dirname(__file__)
RESOURCES = os.path.join(BASE_DIR, "resources")

# ---------------- LOAD IMAGES ----------------
background = pygame.image.load(os.path.join(RESOURCES, "AnimatedStreet.png"))
player_img = pygame.image.load(os.path.join(RESOURCES, "Player.png"))
enemy_img = pygame.image.load(os.path.join(RESOURCES, "Enemy.png"))
coin_img = pygame.image.load(os.path.join(RESOURCES, "coinnn.png"))

# Масштабируем изображения при необходимости
player_img = pygame.transform.scale(player_img, (50, 90))
enemy_img = pygame.transform.scale(enemy_img, (50, 90))
coin_img = pygame.transform.scale(coin_img, (30, 30))

# ---------------- LOAD SOUNDS ----------------
try:
    pygame.mixer.music.load(os.path.join(RESOURCES, "background.wav"))
    pygame.mixer.music.play(-1)

    crash_sound = pygame.mixer.Sound(os.path.join(RESOURCES, "crash.wav"))
except:
    crash_sound = None

# ---------------- FONTS ----------------
font = pygame.font.SysFont("Verdana", 20)
big_font = pygame.font.SysFont("Verdana", 50)

# ---------------- VARIABLES ----------------
score = 0
coins_collected = 0
enemy_speed = 5
coin_speed = 4

# ---------------- PLAYER ----------------
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

# ---------------- ENEMY ----------------
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

        # Если враг ушел вниз — появляется сверху
        if self.rect.top > HEIGHT:
            score += 1
            self.rect.center = (random.randint(50, WIDTH - 50), -100)

# ---------------- COIN ----------------
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_img
        self.rect = self.image.get_rect(
            center=(random.randint(30, WIDTH - 30), random.randint(-500, -50))
        )

    def move(self):
        self.rect.move_ip(0, coin_speed)

        # Если монета ушла вниз — появляется сверху
        if self.rect.top > HEIGHT:
            self.reset()

    def reset(self):
        self.rect.center = (random.randint(30, WIDTH - 30), random.randint(-500, -50))

# ---------------- OBJECTS ----------------
player = Player()
enemy = Enemy()

# Несколько монет
coins = pygame.sprite.Group()
for _ in range(3):
    coin = Coin()
    coins.add(coin)

# Все спрайты
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemy)
all_sprites.add(coins)

# Враги
enemies = pygame.sprite.Group()
enemies.add(enemy)

# ---------------- GAME LOOP ----------------
running = True

while running:
    screen.blit(background, (0, 0))

    # --- EVENTS ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- MOVE OBJECTS ---
    player.move()
    enemy.move()

    for coin in coins:
        coin.move()

    # --- COIN COLLISION ---
    collected = pygame.sprite.spritecollide(player, coins, False)
    for coin in collected:
        coins_collected += 1
        coin.reset()

    # --- ENEMY COLLISION ---
    if pygame.sprite.spritecollideany(player, enemies):
        if crash_sound:
            crash_sound.play()

        screen.fill((255, 0, 0))
        game_over = big_font.render("GAME OVER", True, (0, 0, 0))
        screen.blit(game_over, (80, HEIGHT // 2))
        pygame.display.update()
        time.sleep(2)
        running = False

    # --- DRAW OBJECTS ---
    screen.blit(enemy.image, enemy.rect)
    screen.blit(player.image, player.rect)

    for coin in coins:
        screen.blit(coin.image, coin.rect)

    # --- DRAW TEXT ---
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    coin_text = font.render(f"Coins: {coins_collected}", True, (0, 0, 0))

    screen.blit(score_text, (10, 10))
    screen.blit(coin_text, (280, 10))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
