import pygame
import random
import os

pygame.init()

# ---------------- SETTINGS ----------------
WIDTH = 400
HEIGHT = 600
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")
clock = pygame.time.Clock()

# ---------------- PATHS ----------------
BASE_DIR = os.path.dirname(__file__)
RESOURCES = os.path.join(BASE_DIR, "resources")

# ---------------- IMAGES ----------------
background = pygame.image.load(os.path.join(RESOURCES, "AnimatedStreet.png"))
player_img = pygame.transform.scale(
    pygame.image.load(os.path.join(RESOURCES, "Player.png")), (50, 90)
)
enemy_img = pygame.transform.scale(
    pygame.image.load(os.path.join(RESOURCES, "Enemy.png")), (50, 90)
)

font = pygame.font.SysFont("Verdana", 20)

coins_collected = 0
enemy_speed = 5

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

# ------
