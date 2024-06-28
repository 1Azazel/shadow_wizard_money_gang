# scripts/game_physics.py

import pymunk
import pymunk.pygame_util

def initialize_physics():
    space = pymunk.Space()
    space.gravity = (0, 900)
    return space

def create_static_lines(space, lines):
    for line in lines:
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape = pymunk.Segment(body, line[0], line[1], line[2])
        space.add(body, shape)

def step_physics(space, dt):
    space.step(dt)

def draw_physics(space, screen):
    draw_options = pymunk.pygame_util.DrawOptions(screen)
    space.debug_draw(draw_options)
