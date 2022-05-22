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


def get_order_of_accuracy(method_id: int):
    if method_id == 0:
        return 4
    else:
        return 2


def calculate_final_table_with_accuracy(method_id: int, differential_equation_h: DifferentialEquation, table_h: list, headers_h: list):
    differential_equation_2h = DifferentialEquation(
        differential_equation_h.function_type,
        differential_equation_h.x_0,
        differential_equation_h.y_0,
        differential_equation_h.a,
        differential_equation_h.b,
        differential_equation_h.h / 2
    )
    #print(table_h)
    table_2h, headers_2h = do_method(method_id, differential_equation_2h)
    #print(table_2h)
    table_2h_compressed = []
    for i in range(len(table_2h)):
        if i % 2 == 0:
            #print(table_2h[i][0], table_2h[i][1])
            table_2h_compressed.append(table_2h[i][1])
    for i in range(len(table_h)):
        #print("----", table_h[i][0], table_2h_compressed[i], table_h[i][1])
        table_h[i].append(abs(table_2h_compressed[i] - table_h[i][1]) / ((2**get_order_of_accuracy(method_id)) - 1))
    headers_h.append('accuracy')
    return table_h, headers_h
