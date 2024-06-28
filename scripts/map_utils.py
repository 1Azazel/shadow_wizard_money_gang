# scripts/map_utils.py

import json
from scripts.walls import Wall
from scripts.player import Player


def generate_map():
    walls_data = [
        {"x": 300, "y": 150, "width": 50, "height": 300},
        {"x": 100, "y": 450, "width": 600, "height": 50}
    ]

    map_data = {
        "walls": walls_data
    }

    with open('map.json', 'w') as file:
        json.dump(map_data, file, indent=4)

    print("map.json has been created.")


def save_map(filename, walls):
    walls_data = []
    for wall in walls:
        wall_data = {
            'x': wall.rect.x,
            'y': wall.rect.y,
            'width': wall.rect.width,
            'height': wall.rect.height
        }
        walls_data.append(wall_data)

    map_data = {
        'walls': walls_data
    }

    with open(filename, 'w') as file:
        json.dump(map_data, file)


def load_map(filename):
    with open(filename, 'r') as file:
        map_data = json.load(file)

    walls = []
    for wall_data in map_data['walls']:
        wall = Wall(wall_data['x'], wall_data['y'], wall_data['width'], wall_data['height'])
        walls.append(wall)

    return walls
