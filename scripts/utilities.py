# scripts/utilities.py

import pygame as pg
from settings import *


def init():
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pg.time.Clock()
    font = pg.font.Font(None, FONT_SIZE)
    running = True
    return screen, clock, font, running


def init_player():
    return pg.Rect(PLAYER_START, PLAYER_SIZE)


def move_player(player_rect, move_x, move_y):
    return player_rect.move(int(move_x), int(move_y))


def draw_player(screen, player_color, player_rect):
    pg.draw.rect(screen, player_color, player_rect)
