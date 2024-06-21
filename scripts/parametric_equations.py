from sympy import symbols
import numpy as np

x, y, r, t = symbols("x y r t")


class ParametricEquation:
    def __init__(self, function_of_t):
        self.func = function_of_t


def x_of_t(x0):
    return r * np.cos(t) + x0


def y_of_t(y0):
    return r * np.sin(t) + y0


class SystemOfParametricEquation:
    def __init__(self, func_list, t_range=(-np.inf, np.inf)):
        self.func_list = func_list
        self.t_range = t_range


def get_parametric_eq_of_circle(center, radius):
    function_list = [x_of_t(x), y_of_t(y)]

para_eq_of_circle = SystemOfParametricEquation()


