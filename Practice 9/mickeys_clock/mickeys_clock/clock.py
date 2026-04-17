import pygame
import os
from datetime import datetime


class Clock:
    def __init__(self, screen):
        self.screen = screen
        self.center = (400, 300)

        base_dir = os.path.dirname(__file__)
        hand_path = os.path.join(base_dir, "images", "hand.png")

        
        hand_image = pygame.image.load(hand_path).convert_alpha()

       
        self.second_hand = pygame.transform.scale(hand_image, (400, 80))
        self.minute_hand = pygame.transform.scale(hand_image, (350, 70))

    def get_time(self):
        now = datetime.now()
        return now.minute, now.second

    def draw_hand(self, image, angle):
        rotated = pygame.transform.rotate(image, -angle)
        rect = rotated.get_rect(center=self.center)
        self.screen.blit(rotated, rect)

    def update(self):
        minutes, seconds = self.get_time()

        
        sec_angle = seconds * 6 - 30
        min_angle = minutes * 6 + seconds * 0.1 - 30

        self.draw_hand(self.minute_hand, min_angle)
        self.draw_hand(self.second_hand, sec_angle)
