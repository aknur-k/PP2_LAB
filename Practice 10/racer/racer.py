import pygame, random, time
import os

pygame.init()

# Размер окна
WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Загрузка изображений
BASE_DIR = os.path.dirname(__file__)

background = pygame.image.load(os.path.join(BASE_DIR, "resources", "AnimatedStreet.png"))
player_img = pygame.image.load(os.path.join(BASE_DIR, "resources", "Player.png"))
enemy_img = pygame.image.load(os.path.join(BASE_DIR, "resources", "Enemy.png"))
coin_img = pygame.image.load(os.path.join(BASE_DIR, "resources", "coin.png"))


# Звуки
pygame.mixer.music.load(os.path.join(BASE_DIR, "resources", "background.wav"))
pygame.mixer.music.play(-1)

crash_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "resources", "crash.wav"))


# Шрифты
font = pygame.font.SysFont("Verdana", 20)
big_font = pygame.font.SysFont("Verdana", 60)

score = 0
coins = 0
speed = 5

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect(center=(200, 520))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.move_ip(5, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect(center=(random.randint(40, WIDTH-40), 0))

    def move(self):
        global score, speed
        self.rect.move_ip(0, speed)
        if self.rect.top > HEIGHT:
            score += 1
            self.rect.center = (random.randint(40, WIDTH-40), 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_img
        self.rect = self.image.get_rect(center=(random.randint(40, WIDTH-40), random.randint(50, HEIGHT-50)))

    def reset(self):
        self.rect.center = (random.randint(40, WIDTH-40), random.randint(50, HEIGHT-50))

player = Player()
enemy = Enemy()
coin = Coin()

all_sprites = pygame.sprite.Group(player, enemy, coin)
enemies = pygame.sprite.Group(enemy)

clock = pygame.time.Clock()

running = True
while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # движение игрока и врага
    player.move()
    enemy.move()

    # сбор монет
    if pygame.sprite.collide_rect(player, coin):
        coins += 1
        coin.reset()

    # столкновение с врагом
    if pygame.sprite.spritecollideany(player, enemies):
        crash_sound.play()
        time.sleep(1)
        screen.fill((255, 0, 0))
        game_over = big_font.render("Game Over", True, (0, 0, 0))
        screen.blit(game_over, (70, 250))
        pygame.display.update()
        time.sleep(2)
        running = False

    # отрисовка
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    # счетчики
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    coin_text = font.render(f"Coins: {coins}", True, (0, 0, 0))

    screen.blit(score_text, (10, 10))
    screen.blit(coin_text, (300, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
