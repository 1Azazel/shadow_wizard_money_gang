# settings.py

# Screen Dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
ORIGIN = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

# Font Size
FONT_SIZE = 20

# Frame Rate
TICK = 120

# Player Settings
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_START = ((SCREEN_WIDTH / 2) - (PLAYER_WIDTH / 2), (SCREEN_HEIGHT / 2) - (PLAYER_HEIGHT / 2))
PLAYER_SIZE = (PLAYER_WIDTH, PLAYER_HEIGHT)
PLAYER_SPEED = 300
PLAYER_MASS = 1.0
MOVE_SPEED = 5
ACCELERATION = 0.5

# Environment Settings
FLOOR_FRICTION = 0.1
WALL_FRICTION = 0.2

# Colors (using the palette module)
from palette import test_palette
PALETTE = test_palette.get_colors_in_palette()
SCREEN_COLOR = PALETTE[0]
PLAYER1_COLOR = PALETTE[1]
PLAYER2_COLOR = PALETTE[2]
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Periodic Events
PERIODIC_EVENTS = {
    "0.1s": 100,
    "0.5s": 500,
    "1s": 1000,
    "2s": 2000,
    "3s": 3000,
    "4s": 4000,
    "5s": 5000,
    "10s": 10000,
    "15s": 15000,
    "30s": 30000,
    "45s": 45000,
    "1min": 60000
}
