import pygame
from PIL import Image
import os

pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 30  # Frames per second
EXTENSION = ".gif"
DIRECTORY_PATH = r"C:\Users\xxpun\Documents\GitHub\shadow_wizard_money_gang\game_assets\spell_effect_gifs"
TEST_EFFECTS = [
    "Blue Vortex",
    "Blue Vortex 2",
    "Bonfire",
    "Electric A",
    "Electric B",
    "Fire+Sparks",
    "Fire 1",
    "Fire 2",
    "Fire 3",
    "Flag",
    "Flamethrower",
    "Fly",
    "Grass",
    "Gravity",
    "Leaves",
    "Poison Cloud",
    "Rain1",
    "Rain2",
    "Rocket Fire",
    "Rocket Fire 2",
]

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

class GIFPlayer:
    def __init__(self, gif_path):
        self.gif_path = gif_path
        self.frames = self.load_frames()
        self.current_frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_delay = 100  # milliseconds per frame

    def load_frames(self):
        image = Image.open(self.gif_path)
        frames = []
        for frame in range(0, image.n_frames):
            image.seek(frame)
            frame_image = image.copy().convert('RGBA')
            mode = frame_image.mode
            size = frame_image.size
            data = frame_image.tobytes()
            frame_surface = pygame.image.fromstring(data, size, mode)
            frames.append(frame_surface)
        return frames

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_delay:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.last_update = now

    def draw(self, surface, pos):
        surface.blit(self.frames[self.current_frame], pos)


def get_gif_path(effect_name):
    return os.path.join(DIRECTORY_PATH, effect_name + EXTENSION)


# Load the first GIF
current_effect_index = 0
gif_player = GIFPlayer(get_gif_path(TEST_EFFECTS[current_effect_index]))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                current_effect_index = (current_effect_index + 1) % len(TEST_EFFECTS)
                gif_player = GIFPlayer(get_gif_path(TEST_EFFECTS[current_effect_index]))

    screen.fill((30, 30, 30))

    gif_player.update()
    gif_player.draw(screen, (100, 100))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
