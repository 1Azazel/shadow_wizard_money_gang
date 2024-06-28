# Example file showing a circle moving on screen
import pygame as pg
import numpy as np

i = np.array([[1], [0]])
j = np.array([[0], [1]])
i2 = np.eye(2)


def pythagorean_relationship(num_list):
    sum_of_list = 0
    for num in num_list:
        sum_of_list += (num ** 2)
    return np.sqrt(sum_of_list)

# a and b are scalars
def linear_combination(a, b):
    u = a * i.copy()
    v = b * j.copy()


# Input direction in degrees
class Force:
    def __init__(self, magnitude, direction, x_force=0, y_force=0):
        self.magnitude = magnitude
        self.direction = direction
        self.x_component = x_force
        self.y_component = y_force

    def set_magnitude(self, new_magnitude):
        self.magnitude = new_magnitude

    def get_magnitude(self):
        return self.magnitude

    def update_force(self):
        self.set_magnitude(pythagorean_relationship([self.get_x_force(), self.get_y_force()]))
        self.set_direction(np.tan(self.get_y_force() / self.get_x_force()))

    def set_direction(self, new_direction):
        self.direction = new_direction

    def get_direction(self):
        return self.direction

    def increase_x_force(self):
        self.x_component += 1

    def decrease_x_force(self):
        self.x_component -= 1

    def increase_y_force(self):
        self.y_component += 1

    def decrease_y_force(self):
        self.y_component -= 1

    def get_x_force(self):
        return self.x_component

    def get_y_force(self):
        return self.y_component


class ForceVector:
    def __init__(self, matrix=np.zeros((2, 2))):
        self.matrix = matrix

    def get_matrix(self):
        return self.matrix


class ForcesOnObject:
    def __init__(self, mass):
        self.mass = mass
        self.forces = []

    def add_force(self, magnitude, degrees):
        force = create_force_vector(magnitude, degrees)
        self.forces.append(force)

    def sum_of_forces(self):
        sum_vector = sum_forces(self.forces)
        return sum_vector


def create_force_vector(mag, direction_in_degrees):
    theta = (direction_in_degrees * np.pi) / 180
    x_component = mag * np.cos(theta)
    y_component = mag * np.sin(theta)
    return pg.Vector2(x_component, y_component)


def sum_forces(force_list):
    x_sum = 0
    y_sum = 0
    for force in force_list:
        x_sum += force.x
        y_sum += force.y
    return pg.Vector2(x_sum, y_sum)





"""


dt = 1/60
player_pos = pygame.Vector2((0, 0))


def move_object(screen, clear_screen=False):
    # fill the screen with a color to wipe away anything from last frame
    if clear_screen:
        screen.fill("white")
    pygame.draw.circle(screen, "blue", player_pos, 40)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

"""



