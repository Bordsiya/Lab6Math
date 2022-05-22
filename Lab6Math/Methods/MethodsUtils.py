from Methods.AdamsMethod import adams_method
from Methods.ModifiedEulerMethod import modified_euler_method
from Model.DifferentialEquation import DifferentialEquation

methods_arr = [
    'Метод Адамса',
    'Модифицированный метод Эйлера'
]


def do_method(method_id: int, differential_equation: DifferentialEquation):
    if method_id == 0:
        return adams_method(differential_equation)
    else:
        return modified_euler_method(differential_equation)
