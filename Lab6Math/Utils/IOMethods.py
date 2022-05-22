from tabulate import tabulate

from Methods.MethodsUtils import methods_arr
from Model.DifferentialEquation import DifferentialEquation, function_types_arr, get_function, get_initial_condition, \
    get_interval, intervals_arr, initial_conditions_arr
from Utils.Exceptions import exceptions_arr


def get_data() -> DifferentialEquation:
    function_type = get_input_function()
    x0, y0 = get_initial_condition(function_type)
    a, b = get_interval(function_type)
    h = get_step()
    #e = get_accuracy()
    return DifferentialEquation(function_type, x0, y0, a, b, h)


def get_input_function() -> int:
    print("Выберите задачу из списка:")
    for i in range(len(function_types_arr)):
        print("(", i, ")", function_types_arr[i], "на", intervals_arr[i], "при", initial_conditions_arr[i])
    func_type = input().strip()
    try:
        func_type = int(func_type)
        if func_type >= len(function_types_arr) or func_type < 0:
            print("Ошибка: ", exceptions_arr['WrongLimitsArgument'])
            exit(1)
    except ValueError:
        print('Ошибка: ', exceptions_arr['ValueError'])
        exit(1)

    return func_type


def get_step() -> float:
    h = input("Введите шаг h: ").strip().replace(',', '.')
    try:
        h = float(h)
        if h <= 0:
            print('Ошибка: ', exceptions_arr['NegativeStepException'])
            exit(1)
    except ValueError:
        print('Ошибка: ', exceptions_arr['ValueError'])
        exit(1)

    return h


#def get_accuracy() -> float:
#    e = input('Введите погрешность вычисления: ').strip()
#    try:
#        e = float(e.replace(',', '.'))
#        if e < 0:
#            print('Ошибка: ', exceptions_arr['NegativeAccuracy'])
#            exit(1)
#    except ValueError:
#        print('Ошибка: ', exceptions_arr['ValueError'])
#        exit(1)
#
#    return e


def get_method() -> int:
    print("Выберите метод для решения:")
    for i in range(len(methods_arr)):
        print("(", i, ")", methods_arr[i])

    method_id = input().strip()
    try:
        method_id = int(method_id)
        if method_id >= len(function_types_arr) or method_id < 0:
            print("Ошибка: ", exceptions_arr['WrongLimitsArgument'])
            exit(1)
    except ValueError:
        print('Ошибка: ', exceptions_arr['ValueError'])
        exit(1)

    return method_id


def print_table(table: list, headers: list):
    print("Таблица приближенных значений интеграла:")
    print(tabulate(table, headers, tablefmt="github"))
