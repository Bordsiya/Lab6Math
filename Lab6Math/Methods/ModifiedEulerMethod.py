from Model.DifferentialEquation import DifferentialEquation, get_function


def modified_euler_method(differential_equation: DifferentialEquation):
    f = get_function(differential_equation.function_type)
    h = differential_equation.h
    table = []
    headers = ["x", "y", "f(x, y)", "y_exemplary", "f(x, y_exemplary)"]
    y_pred = differential_equation.y_0
    x_pred = differential_equation.x_0
    table.append([x_pred, y_pred, f(x_pred, y_pred)])

    x_curr = differential_equation.a
    while x_curr <= differential_equation.b:
        x_curr += h
        y_exemplary = y_pred + h * f(x_pred, y_pred)
        y_curr = y_pred + (h / 2) * (f(x_pred, y_pred) + f(x_curr, y_exemplary))
        table.append([x_curr, y_curr, f(x_curr, y_curr), y_exemplary, f(x_curr, y_exemplary)])
        x_pred = x_curr
        y_pred = y_curr

    return table, headers
