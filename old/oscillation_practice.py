import pygame as pg
import numpy as np
import sys

from palette import test_palette

# Global Variables

# Screen Dimensions
WIDTH = 800
HEIGHT = 800
ORIGIN = (WIDTH/2, HEIGHT/2)

FONT_SIZE = 20

TICK = 120

PLAYER_WIDTH = 20
PLAYER_HEIGHT = 40
PLAYER_START = ((WIDTH/2) - (PLAYER_WIDTH/2), (HEIGHT/2) - (PLAYER_HEIGHT/2))
PLAYER_SIZE = (PLAYER_WIDTH, PLAYER_HEIGHT)
PLAYER_SPEED = 300

PLAYER1_MIN_X = 0
PLAYER1_MAX_X = 0
PLAYER1_MIN_Y = 0
PLAYER1_MAX_Y = 0

PLAYER2_MIN_X = 0
PLAYER2_MAX_X = 0
PLAYER2_MIN_Y = 0
PLAYER2_MAX_Y = 0

PALETTE = test_palette.get_colors_in_palette()
SCREEN_COLOR = PALETTE[0]
PLAYER1_COLOR = PALETTE[1]
PLAYER2_COLOR = PALETTE[2]

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


# Initialize Game
def init():
    pg.init()  # initiating pygame
    screen = pg.display.set_mode((WIDTH, HEIGHT))  # creating the display surface
    clock = pg.time.Clock()  # creating the game clock
    origin = (WIDTH/2, HEIGHT/2)
    font = pg.font.Font(None, FONT_SIZE)
    running = True
    return screen, clock, origin, font, running


# Placeholder PLayer Functions
def init_player():
    return pg.Rect(PLAYER_START, PLAYER_SIZE)


def get_radius_of_largest_possible_circle():
    if WIDTH >= HEIGHT:
        r = HEIGHT/2
    else:
        r = WIDTH/2
    return r


def map_to_center_of_screen(old_pos):
    old_x, old_y = old_pos
    x = old_x + (WIDTH/2)
    y = old_y + (HEIGHT/2)
    new_pos = (x, y)
    return new_pos


def move_player(player_rect, move_x, move_y):
    return player_rect.move(int(move_x), int(move_y))


def draw_player(screen, player_color, player_rect):
    pg.draw.rect(screen, player_color, player_rect)


def get_theta(time_now, periodicity):
    period = PERIODIC_EVENTS[periodicity]
    theta = (2 * np.pi) * (time_now / period)
    print(round(theta, 2))
    return theta


def x_movement_func(r, t):
    theta = get_theta(t, "2s")
    return r * np.sin(theta) + (WIDTH / 2)


def y_movement_func(r, t):
    theta = get_theta(t, "3s")
    return r * np.sin(theta) + (HEIGHT / 2)


def get_pos(r, theta):
    x = r * np.sin(theta)
    y = r * np.cos(theta)
    pos = (x, y)
    print(pos)
    return pos


def oscillate(t):
    theta = get_theta(t, "4s")
    x = np.cos(theta)
    coord = (x, 0)
    return coord


def draw_horizontal_oscillation(t, r, screen, color, player):
    move_to_x = x_movement_func(r, t)
    player.x = move_to_x
    draw_player(screen, color, player)


def draw_vertical_oscillation(t, r, screen, color, player):
    move_to_y = y_movement_func(r, t)
    player.y = move_to_y
    draw_player(screen, color, player)


def draw_oscillating_movement(t, r, screen, color, player):
    theta = get_theta(t, "4s")
    pos = get_pos(r, theta)
    move_x, move_y = pos
    move_player(player, move_x, move_y)
    draw_player(screen, color, player)


def time_count(time_now):
    time_in_s = time_now / 1000
    time_str = "Time: " + str(round(time_in_s, 1))
    return time_str


def check_collision(p1_rect, p2_rect):
    collision_state = p1_rect.colliderect(p2_rect)
    return collision_state


def get_collision_string(p1_rect, p2_rect):
    collision_state = check_collision(p1_rect, p2_rect)
    if collision_state is True:
        return "Collision Detected"
    else:
        return "No Collision Detected"


def check_range(player_rect, player_min_x, player_max_x, player_min_y, player_max_y):

    pos_x = player_rect.centerx
    pos_y = player_rect.centery

    if pos_x < player_min_x:
        player_min_x = pos_x
    if pos_x > player_max_x:
        player_max_x = pos_x
    if pos_y < player_min_y:
        player_min_y = pos_y
    if pos_y > player_max_y:
        player_max_y = pos_y

    x_range = [player_min_x, player_max_x]
    y_range = [player_min_y, player_max_y]

    return x_range, y_range


def main():
    screen, clock, origin, font, running = init()
    r_max = get_radius_of_largest_possible_circle()
    player1_rect = init_player()
    player2_rect = player1_rect.copy()

    p1_x_range = [0, 0]
    p1_y_range = [0, 0]
    p2_x_range = [0, 0]
    p2_y_range = [0, 0]

    collision_state = False
    num_collisions = 0
    collision_string = "Number of Collisions: " + str(num_collisions)

    # Run Game Loop
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        screen.fill(SCREEN_COLOR)

        time_now = pg.time.get_ticks()

        draw_horizontal_oscillation(time_now, r_max, screen, PLAYER1_COLOR, player1_rect)
        draw_vertical_oscillation(time_now, r_max, screen, PLAYER2_COLOR, player2_rect)
        previous_collision_state = collision_state
        collision_state = check_collision(player1_rect, player2_rect)
        if collision_state is False:
            if previous_collision_state is True:
                num_collisions += 1
                collision_string = "Number of Collisions: " + str(num_collisions)

        p1_x_range, p1_y_range = check_range(player1_rect, PLAYER1_MIN_X, PLAYER1_MAX_X, PLAYER1_MIN_Y, PLAYER1_MAX_Y)
        p2_x_range, p2_y_range = check_range(player2_rect, PLAYER2_MIN_X, PLAYER2_MAX_X, PLAYER2_MIN_Y, PLAYER2_MAX_Y)

        screen.blit(font.render(time_count(time_now), True, pg.Color(PALETTE[3])), (5, 5))
        screen.blit(font.render(get_collision_string(player1_rect, player2_rect), True, pg.Color(PALETTE[3])), (5, 30))
        screen.blit(font.render(collision_string, True, pg.Color(PALETTE[3])), (5, 55))

        pg.display.flip()
        dt = clock.tick(TICK) / 1000

    # Game Exit
    print("\nPlayer 1: ")
    print("X Range: " + str(p1_x_range[0]) + ", " + str(p1_x_range[1]))
    print("Y Range: " + str(p1_y_range[0]) + ", " + str(p1_y_range[1]))

    print("\nPlayer 2: ")
    print("X Range: " + str(p2_x_range[0]) + ", " + str(p2_x_range[1]))
    print("Y Range: " + str(p2_y_range[0]) + ", " + str(p2_y_range[1]))

    print("\nQuitting Game")
    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()

