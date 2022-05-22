from Methods.RungeKutta4Method import runge_kutta_4_method
from Model.DifferentialEquation import DifferentialEquation, get_function

acc = 14


def adams_method(differential_equation: DifferentialEquation):
    if ((differential_equation.b - differential_equation.a) / differential_equation.h) + 1 <= 4:
        return runge_kutta_4_method(differential_equation)

    table =[]
    headers = ["x", "y", "fi", "lambda_fi", "lambda2_fi", "lambda3_fi"]

    h = differential_equation.h
    f = get_function(differential_equation.function_type)
    table_runge, headers_runge = runge_kutta_4_method(differential_equation)
    x_precalculated = []
    [x_precalculated.append(l[:1][0]) for l in table_runge[:4]]
    y_precalculated = []
    [y_precalculated.append(l[1:2][0]) for l in table_runge[:4]]
    for i in range(4):
        table.append([x_precalculated[i], y_precalculated[i], '', '', '', ''])

    x_curr = x_precalculated[3]
    while x_curr < differential_equation.b:
        x_curr += h
        if round(x_curr, acc) > differential_equation.b:
            break
        lambda_fi = f(x_precalculated[3], y_precalculated[3]) - f(x_precalculated[2], y_precalculated[2])
        lambda2_fi = f(x_precalculated[3], y_precalculated[3]) - 2 * f(x_precalculated[2], y_precalculated[2]) \
                    + f(x_precalculated[1], y_precalculated[1])
        lambda3_fi = f(x_precalculated[3], y_precalculated[3]) - 3 * f(x_precalculated[2], y_precalculated[2]) \
                    + 3 * f(x_precalculated[1], y_precalculated[1]) - f(x_precalculated[0], y_precalculated[0])
        y_curr = y_precalculated[3] + h * f(x_precalculated[3], y_precalculated[3]) \
                + ((h**2) / 2) * lambda_fi + ((5 * h**3) / 12) * lambda2_fi + ((3 * h**4) / 8) * lambda3_fi
        table.append([x_curr, y_curr, f(x_precalculated[3], y_precalculated[3]), lambda_fi, lambda2_fi, lambda3_fi])
        for i in range(1, 4):
            x_precalculated[i - 1] = x_precalculated[i]
            y_precalculated[i - 1] = y_precalculated[i]
        x_precalculated[3] = x_curr
        y_precalculated[3] = y_curr

    return table, headers
