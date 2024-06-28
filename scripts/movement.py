# scripts/movement.py

import pygame as pg
from settings import *


def map_to_center_of_screen(old_pos):
    old_x, old_y = old_pos
    x = old_x + (SCREEN_WIDTH / 2)
    y = old_y + (SCREEN_HEIGHT / 2)
    return x, y


def handle_player_movement(player_rect, keys_pressed):
    if keys_pressed[pg.K_a]:
        player_rect.x -= PLAYER_SPEED
    if keys_pressed[pg.K_d]:
        player_rect.x += PLAYER_SPEED
    if keys_pressed[pg.K_w]:
        player_rect.y -= PLAYER_SPEED
    if keys_pressed[pg.K_s]:
        player_rect.y += PLAYER_SPEED


def constrain_player_to_screen(player_rect):
    if player_rect.left < 0:
        player_rect.left = 0
    if player_rect.right > SCREEN_WIDTH:
        player_rect.right = SCREEN_WIDTH
    if player_rect.top < 0:
        player_rect.top = 0
    if player_rect.bottom > SCREEN_HEIGHT:
        player_rect.bottom = SCREEN_HEIGHT
