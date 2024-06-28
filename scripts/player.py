# scripts/player.py

import pygame
from pygame.math import Vector2
from settings import (PLAYER_SIZE, WHITE, SCREEN_WIDTH, SCREEN_HEIGHT, ACCELERATION, FLOOR_FRICTION, MOVE_SPEED,
                      PLAYER_MASS)


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface(PLAYER_SIZE)
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.position = Vector2(x, y)
        self.velocity = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)
        self.mass = PLAYER_MASS

    def update(self):
        keys = pygame.key.get_pressed()
        self.acceleration = Vector2(0, 0)

        if keys[pygame.K_w]:
            self.acceleration.y = -ACCELERATION
        if keys[pygame.K_s]:
            self.acceleration.y = ACCELERATION
        if keys[pygame.K_a]:
            self.acceleration.x = -ACCELERATION
        if keys[pygame.K_d]:
            self.acceleration.x = ACCELERATION

        # Apply floor friction
        self.acceleration += self.velocity * -FLOOR_FRICTION

        # Update velocity and position
        self.velocity += self.acceleration
        if self.velocity.length() > MOVE_SPEED:
            self.velocity.scale_to_length(MOVE_SPEED)

        self.position += self.velocity + 0.5 * self.acceleration
        self.rect.topleft = self.position

        # Check screen boundaries
        if self.rect.left < 0:
            self.rect.left = 0
            self.velocity.x = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.velocity.x = 0
        if self.rect.top < 0:
            self.rect.top = 0
            self.velocity.y = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.velocity.y = 0

    def handle_collision(self, walls):
        collisions = pygame.sprite.spritecollide(self, walls, False)
        for wall in collisions:
            self.conserve_momentum(wall)

    def conserve_momentum(self, wall):
        wall_mass = float('inf')  # Assuming the wall has infinite mass

        if self.velocity.x > 0:  # Moving right
            self.rect.right = wall.rect.left
        if self.velocity.x < 0:  # Moving left
            self.rect.left = wall.rect.right
        if self.velocity.y > 0:  # Moving down
            self.rect.bottom = wall.rect.top
        if self.velocity.y < 0:  # Moving up
            self.rect.top = wall.rect.bottom

        # Update the position after handling the collision
        self.position = Vector2(self.rect.topleft)

        # Calculate the final velocity after collision
        if self.velocity.length() != 0:
            normal = (Vector2(self.rect.center) - Vector2(wall.rect.center)).normalize()
            relative_velocity = self.velocity - Vector2(0, 0)
            normal_velocity = relative_velocity.dot(normal) * normal
            self.velocity -= 2 * (self.mass / (self.mass + wall_mass)) * normal_velocity

    def draw(self, screen):
        screen.blit(self.image, self.rect)
