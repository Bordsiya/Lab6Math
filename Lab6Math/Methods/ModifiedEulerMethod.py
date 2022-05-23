from Model.Answer import Answer
from Model.DifferentialEquation import DifferentialEquation, get_function

acc = 14


def modified_euler_method(differential_equation: DifferentialEquation, NMAX: int, y_acc) -> Answer:
    if ((differential_equation.b - differential_equation.a) // differential_equation.h) + 1 > NMAX:
        return Answer(None, None, False, "Слишком большое число узлов")

    f = get_function(differential_equation.function_type)
    h = differential_equation.h
    table = []
    headers = ["x", "y", "f(x, y)", "y_exemplary", "f(x, y_exemplary)", "y_acc", "e"]
    y_pred = differential_equation.y_0
    x_pred = differential_equation.x_0
    table.append([x_pred, y_pred, f(x_pred, y_pred), '', '', y_acc(x_pred), 0])

    x_curr = differential_equation.a
    while x_curr < differential_equation.b:
        try:
            x_curr += h
            if round(x_curr, acc) > differential_equation.b:
                break
            y_exemplary = y_pred + h * f(x_pred, y_pred)
            y_curr = y_pred + (h / 2) * (f(x_pred, y_pred) + f(x_curr, y_exemplary))
            table.append([x_curr, y_curr, f(x_curr, y_curr), y_exemplary, f(x_curr, y_exemplary), y_acc(x_curr), abs(y_curr - y_acc(x_curr))])
            x_pred = x_curr
            y_pred = y_curr
            if abs(y_curr - y_acc(x_curr)) > differential_equation.e:
                return Answer(table, headers, False, "Слишком большой шаг")
        except OverflowError:
            return Answer(None, None, False, "Слишком большие числа")

    return Answer(table, headers, True, "")
