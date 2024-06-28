import pygame
from pygame.math import Vector2

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Player constants
PLAYER_SIZE = (50, 50)
ACCELERATION = 0.5
FLOOR_FRICTION = -0.12
MOVE_SPEED = 10
PLAYER_MASS = 1

# Wall class for testing
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect(topleft=(x, y))

# Player class with updated bounce logic
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface(PLAYER_SIZE)
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.position = Vector2(x, y)
        self.velocity = Vector2(5, 2)
        self.acceleration = Vector2(0, 0)
        self.mass = PLAYER_MASS

    def update(self):
        self.acceleration = Vector2(0, 0)

        # Apply floor friction
        self.acceleration += self.velocity * FLOOR_FRICTION

        # Update velocity and position
        self.velocity += self.acceleration
        if self.velocity.length() > MOVE_SPEED:
            self.velocity.scale_to_length(MOVE_SPEED)

        self.position += self.velocity + 0.5 * self.acceleration
        self.rect.topleft = self.position

        # Check screen boundaries
        if self.rect.left < 0:
            self.rect.left = 0
            self.velocity.x = -self.velocity.x
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.velocity.x = -self.velocity.x
        if self.rect.top < 0:
            self.rect.top = 0
            self.velocity.y = -self.velocity.y
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.velocity.y = -self.velocity.y

    def handle_collision(self, walls):
        collisions = pygame.sprite.spritecollide(self, walls, False)
        for wall in collisions:
            if self.velocity.length() == 0:
                continue  # Skip if velocity is zero

            # Calculate reflection vector
            normal = Vector2(0, 0)
            if self.rect.right > wall.rect.left and self.rect.left < wall.rect.right:
                if self.rect.bottom > wall.rect.top and self.rect.top < wall.rect.bottom:
                    if self.velocity.x > 0:
                        normal.x = -1
                    elif self.velocity.x < 0:
                        normal.x = 1
                    if self.velocity.y > 0:
                        normal.y = -1
                    elif self.velocity.y < 0:
                        normal.y = 1

            self.velocity = self.velocity.reflect(normal)
            self.position += self.velocity
            self.rect.topleft = self.position

# Setup for testing
def test_bouncing_player():
    pygame.init()
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    walls = pygame.sprite.Group()

    # Create walls
    wall1 = Wall(300, 100, 200, 20)
    wall2 = Wall(300, 400, 200, 20)
    walls.add(wall1, wall2)
    all_sprites.add(wall1, wall2)

    # Create player
    player = Player(100, 100)
    all_sprites.add(player)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update()
        player.handle_collision(walls)

        screen.fill(WHITE)
        all_sprites.draw(screen)
        pygame.display.flip()

        clock.tick(30)

    pygame.quit()

# Run the test
test_bouncing_player()
