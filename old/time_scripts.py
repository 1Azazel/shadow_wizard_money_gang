import time as t
import numpy as np


def get_time_dif(time_start, time_now):
    return time_now - time_start


def get_fraction_of_elapsed_time(time_start, time_now, time_interval):
    elapsed_time = get_time_dif(time_start, time_now)
    fractional_time = elapsed_time / time_interval
    return fractional_time
