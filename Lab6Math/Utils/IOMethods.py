from tabulate import tabulate

from Methods.MethodsUtils import methods_arr, N_MAX
from Model.DifferentialEquation import DifferentialEquation, function_types_arr, get_function, get_initial_condition, \
    get_interval, intervals_arr, initial_conditions_arr, get_acc_function
from Utils.Exceptions import exceptions_arr


def get_data() -> DifferentialEquation:
    function_type = get_input_function()
    x0, y0 = get_initial_conditions(function_type)
    a = x0
    b = get_right_interval(a)
    h = get_step(a, b)
    e = get_accuracy()
    return DifferentialEquation(function_type, x0, y0, a, b, h, e)


def get_input_function() -> int:
    print("Выберите задачу из списка:")
    for i in range(len(function_types_arr)):
        print("(", i, ")", function_types_arr[i])
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


def get_initial_conditions(function_type: int):
    print("Примерные точки:")
    f_acc = get_acc_function(function_type)
    x_acc = get_initial_condition(function_type)[0]
    for i in range(x_acc, x_acc + 3):
        print("x =", i, ",y =", round(f_acc(i), 3))

    x0 = input("Введите x0: ")
    try:
        x0 = float(x0)
    except ValueError:
        print('Ошибка: ', exceptions_arr['ValueError'])
        exit(1)

    y0 = input("Введите y0: ")
    try:
        y0 = float(y0)
        for i in range(x_acc, x_acc + 3):
            if y0 == round(f_acc(i), 3):
                y0 = f_acc(i)
                break
    except ValueError:
        print('Ошибка: ', exceptions_arr['ValueError'])
        exit(1)

    if f_acc(x0) != y0:
        print("Ошибка: ", exceptions_arr['IncorrectTask'])
        exit(1)

    return x0, y0


def get_right_interval(left_interval: float):
    right_interval = input("Введите правую границу для интервала: ")
    try:
        right_interval = float(right_interval)
        if right_interval < left_interval:
            print('Ошибка: ', exceptions_arr['RightIntervalLowerThanLeft'])
            exit(1)
    except ValueError:
        print('Ошибка: ', exceptions_arr['ValueError'])
        exit(1)

    return right_interval


def get_step(a: float, b: float) -> float:
    h = input("Введите шаг h: ").strip().replace(',', '.')
    try:
        h = float(h)
        if h <= 0:
            print('Ошибка: ', exceptions_arr['NegativeStepException'])
            exit(1)
    except ValueError:
        print('Ошибка: ', exceptions_arr['ValueError'])
        exit(1)

    if (abs(b - a) // h) + 1 > N_MAX or abs(b - a) // (h / 2) + 1 > N_MAX:
        print('Ошибка: ', exceptions_arr['TooManyPoints'], (abs(b - a) // h) + 1)
        exit(1)

    return h


def get_accuracy() -> float:
    e = input('Введите погрешность вычисления: ').strip()
    try:
        e = float(e.replace(',', '.'))
        if e < 0:
            print('Ошибка: ', exceptions_arr['NegativeAccuracy'])
            exit(1)
    except ValueError:
        print('Ошибка: ', exceptions_arr['ValueError'])
        exit(1)

    return e


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
