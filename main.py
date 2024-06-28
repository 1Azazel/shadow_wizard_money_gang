# main.py

import pygame as pg
import sys
from settings import *
from scripts.utilities import init
from scripts.player import Player
from scripts.walls import Wall
from scripts.map_utils import save_map, load_map


def main():
    screen, clock, font, running = init()

    # Create sprite groups
    all_sprites = pg.sprite.Group()
    walls = pg.sprite.Group()

    # Load walls from a map file
    loaded_walls = load_map('map.json')
    for wall in loaded_walls:
        walls.add(wall)
        all_sprites.add(wall)

    # Create player
    player = Player(100, 100)
    all_sprites.add(player)

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        all_sprites.update()

        # Collision detection and handling
        player.handle_collision(walls)

        screen.fill(SCREEN_COLOR)

        # Draw all sprites
        for entity in all_sprites:
            entity.draw(screen)

        pg.display.flip()
        clock.tick(TICK)

    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()
