# scripts/enemy.py

import pygame
from pygame.math import Vector2
from settings import ENEMY_SIZE, ENEMY_COLOR, ENEMY_SPEED

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface(ENEMY_SIZE)
        self.image.fill(ENEMY_COLOR)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.position = Vector2(x, y)
        self.velocity = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)

    def update(self):
        # Define enemy movement logic here
        self.position += self.velocity
        self.rect.topleft = self.position

    def handle_collision(self, walls):
        # Similar collision handling logic as the player
        collisions = pygame.sprite.spritecollide(self, walls, False)
        for wall in collisions:
            self.conserve_momentum(wall)

    def conserve_momentum(self, wall):
        # Similar momentum conservation logic as the player
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)
