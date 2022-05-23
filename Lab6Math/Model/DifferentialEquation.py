from dataclasses import dataclass
import numpy as np


@dataclass
class DifferentialEquation:
    function_type: int
    x_0: float
    y_0: float
    a: float
    b: float
    h: float
    e: float


function_types_arr = [
    'y\' = y + (1 + x)y^2',
    'y\' = x^2 - 2y',
    'y\' = xy^2'
]


intervals_arr = [
    '[1; 1.5]',
    '[0; 3]',
    '[0; 1]'
]


initial_conditions_arr = [
    'y(1) = -1',
    'y(0) = 1',
    'y(0) = 1'
]


acc_function_arr = [
    'y_acc(x) = -1 / x',
    'y_acc(x) = (3 / (4 * e^(2 * x))) + (x^2) / 2 - x / 2 + 1 / 4',
    'y_acc(x) = -2 / (x^2 - 2)'
]


def get_function(func_id: int):
    if func_id == 0:
        return lambda x, y: y + (1 + x) * (y**2)
    elif func_id == 1:
        return lambda x, y: x**2 - 2 * y
    else:
        return lambda x, y: x * (y**2)


def get_interval(func_id: int):
    if func_id == 0:
        return 1, 1.5
    elif func_id == 1:
        return 0, 3
    else:
        return 0, 1


def get_initial_condition(func_id: int):
    if func_id == 0:
        return 1, -1
    elif func_id == 1:
        return 0, 1
    else:
        return 0, 1


def get_acc_function(func_id):
    if func_id == 0:
        return lambda x: -1 / x
    elif func_id == 1:
        return lambda x: (3 / (4 * np.exp(2 * x))) + (x**2) / 2 - x / 2 + 1 / 4
    else:
        return lambda x: -2 / ((x**2) - 2)
