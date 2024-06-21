import pygame as pg
import numpy as np


def draw_player_at(pos):
    pass


def get_player_input():
    last_key = ""
    presses = 0
    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        presses += 1
    if keys[pg.K_s]:
        presses += 1
    if keys[pg.K_a]:
        presses += 1
    if keys[pg.K_d]:
        presses += 1


def move_player(player_pos, player_speed, dt):
    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        player_pos.y -= player_speed * dt
    if keys[pg.K_s]:
        player_pos.y += player_speed * dt
    if keys[pg.K_a]:
        player_pos.x -= player_speed * dt
    if keys[pg.K_d]:
        player_pos.x += player_speed * dt

