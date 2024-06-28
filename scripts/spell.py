# scripts/spell.py

import pygame
from pygame.math import Vector2
from settings import SPELL_SIZE, SPELL_COLOR

class Spell(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity):
        super().__init__()
        self.image = pygame.Surface(SPELL_SIZE)
        self.image.fill(SPELL_COLOR)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.position = Vector2(x, y)
        self.velocity = Vector2(velocity)

    def update(self):
        self.position += self.velocity
        self.rect.topleft = self.position

    def handle_collision(self, targets):
        collisions = pygame.sprite.spritecollide(self, targets, False)
        for target in collisions:
            # Handle spell collision with targets
            pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)
