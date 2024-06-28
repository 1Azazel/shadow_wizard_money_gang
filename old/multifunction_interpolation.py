import pygame as pg
import numpy as np

def get_average_of_two_functions(value, func1, func2):
    value1 = func1(value)
    value2 = func2(value)
    avg_value = (value1 + value2) / 2
    return avg_value

def get_weighted_average_of_time_oscillating_functions(func1, func2):
    def wrapper():



