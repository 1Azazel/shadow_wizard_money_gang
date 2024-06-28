import numpy as np
import math as m


# noinspection PyPep8Naming

class CosmicBody:
    GRAV_CONSTANT = 10
    MASS_OF_STAR = 100
    MASS_OF_SATELLITE = 10
    RADIUS = 100

    def __init__(self, name, mass=MASS_OF_SATELLITE, radius=100):
        self.name = name
        self.mass = mass
        self.velocity = self.get_velocity()
        self.acceleration = self.get_acceleration()
        self.radius = radius
        self.f_net = self.get_f_net()
        self.period = self.get_T()

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

    def set_mass(self, new_mass):
        self.mass = new_mass

    def get_mass(self):
        return self.mass

    def set_velocity(self, new_velocity):
        self.velocity = new_velocity

    def get_velocity(self):
        return np.sqrt((self.GRAV_CONSTANT * self.MASS_OF_STAR) / self.radius)

    def set_acceleration(self, new_acceleration):
        self.acceleration = new_acceleration

    def get_acceleration(self):
        return (self.GRAV_CONSTANT * self.MASS_OF_STAR) / (self.radius ** 2)

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_radius(self):
        return self.radius

    def get_f_net(self):
        f_net = (self.mass * (self.velocity ** 2)) / self.radius
        return f_net

    def get_f_grav(self):
        f_grav = (self.GRAV_CONSTANT * self.mass * self.MASS_OF_STAR) / (self.radius ** 2)
        return f_grav

    def set_T(self, new_T):
        self.period = new_T

    def get_T(self):
        return np.sqrt((self.radius ** 3) * ((4 * (np.pi ** 2)) / (self.GRAV_CONSTANT * self.MASS_OF_STAR)))

    def get_radius_as_function_of_T(self):
        r = pow(((self.period ** 2) * ((self.GRAV_CONSTANT * self.MASS_OF_STAR) / (4 * (np.pi ** 2)))), (1/3))
        return r

    def display_information(self):
        print("Radius of Orbit: " + str(round(self.get_radius())))
        print(f"Velocity of {self.get_name()}: " + str(round(self.get_velocity())))
        print("Acceleration: " + str(round(self.get_acceleration())))
        print("Period: " + str(round(self.period)))
        print("Mass: " + str(round(self.get_mass())))
        print("Gravitational Constant: " + str(round(self.GRAV_CONSTANT)))








