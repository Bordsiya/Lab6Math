from Model.DifferentialEquation import DifferentialEquation, get_function


def runge_kutta_4_method(differential_equation: DifferentialEquation):
    f = get_function(differential_equation.function_type)
    h = differential_equation.h
    table = []
    headers = ["x", "y", "k1", "k2", "k3", "k4"]
    y_pred = differential_equation.y_0
    x_pred = differential_equation.x_0

    x_curr = differential_equation.a
    while x_curr <= differential_equation.b:
        x_curr += h
        k1 = h * f(x_pred, y_pred)
        k2 = h * f(x_pred + (h / 2), y_pred + (k1 / 2))
        k3 = h * f(x_pred + (h / 2), y_pred + (k2 / 2))
        k4 = h * f(x_pred + h, y_pred + k3)
        y_curr = y_pred + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        table.append([x_pred, y_pred, k1, k2, k3, k4])
        y_pred = y_curr
        x_pred = x_curr

    return table, headers
