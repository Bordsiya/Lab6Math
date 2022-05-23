from tabulate import tabulate

from Methods.AdamsMethod import adams_method
from Methods.ModifiedEulerMethod import modified_euler_method
from Model.DifferentialEquation import DifferentialEquation, get_acc_function

methods_arr = [
    'Метод Адамса',
    'Модифицированный метод Эйлера'
]


N_MAX = 5000


def do_method(method_id: int, differential_equation: DifferentialEquation):
    if method_id == 0:
        return adams_method(differential_equation, N_MAX, get_acc_function(differential_equation.function_type))
    else:
        return modified_euler_method(differential_equation, N_MAX, get_acc_function(differential_equation.function_type))


def get_order_of_accuracy(method_id: int):
    if method_id == 0:
        return 4
    else:
        return 2


def calculate_final_table_with_accuracy(method_id: int, differential_equation_h: DifferentialEquation):

    '''h_curr = differential_equation_h.h
    pred_acc = [0] * len(table_h)
    step = 1
    while True:
        h_curr /= 2
        step *= 2
        differential_equation_2h = DifferentialEquation(
            differential_equation_h.function_type,
            differential_equation_h.x_0,
            differential_equation_h.y_0,
            differential_equation_h.a,
            differential_equation_h.b,
            h_curr,
            differential_equation_h.e
        )
        print(table_h)
        table_2h, headers_2h = do_method(method_id, differential_equation_2h)
        if table_2h is None:
            break
        print(table_2h)
        table_2h_compressed = []
        for i in range(len(table_2h)):
            if i % step == 0:
                print(table_2h[i][0], table_2h[i][1])
                table_2h_compressed.append(table_2h[i][1])
        acc_arr = []
        for i in range(len(table_h)):
            if step == 2:
                print("----", table_h[i][0], table_2h_compressed[i], table_h[i][1])
                acc_arr.append(
                    abs(table_2h_compressed[i] - table_h[i][1]) / ((2 ** get_order_of_accuracy(method_id)) - 1))
            else:
                print("----", table_h[i][0], table_2h_compressed[i], table_h[i][len(headers_h) - 1])
                acc_arr.append(
                    abs(table_2h_compressed[i] - table_h[i][len(headers_h) - 1]) / ((2 ** get_order_of_accuracy(method_id)) - 1))
            table_h[i].append(table_2h_compressed[i])

        mx_accuracy = max(acc_arr)
        pred_acc = acc_arr
        #print("max_accuracy: ", mx_accuracy, "h_curr:", h_curr)
        print(table_h)
        headers_h.append('new_y')
        if mx_accuracy < differential_equation_h.e:
            break
    headers_h.append('accuracy')
    for i in range(len(table_h)):
        table_h[i].append(pred_acc[i])
    return table_h, headers_h
    '''

    h_curr = differential_equation_h.h
    while True:
        print("Шаг =", h_curr)
        differential_equation = DifferentialEquation(
            differential_equation_h.function_type,
            differential_equation_h.x_0,
            differential_equation_h.y_0,
            differential_equation_h.a,
            differential_equation_h.b,
            h_curr,
            differential_equation_h.e
        )
        ans = do_method(method_id, differential_equation)
        if ans.table is not None:
            print("Таблица приближенных значений интеграла:")
            print(tabulate(ans.table, ans.headers, tablefmt="github"))
        if ans.message == "Слишком большой шаг":
            h_curr /= 2
        else:
            break
    return ans.table, ans.headers
