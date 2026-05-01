import pygame

class Ball:
    def __init__(self, width, height):
        self.x = width // 2
        self.y = height // 2
        self.radius = 25
        self.width = width
        self.height = height

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy

        if self.radius <= new_x <= self.width - self.radius:
            self.x = new_x
        if self.radius <= new_y <= self.height - self.radius:
            self.y = new_y

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 128, 190), (self.x, self.y), self.radius)
