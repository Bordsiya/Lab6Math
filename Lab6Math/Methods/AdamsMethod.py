
from Methods.ModifiedEulerMethod import modified_euler_method
from Model.Answer import Answer
from Model.DifferentialEquation import DifferentialEquation, get_function

acc = 14


def adams_method(differential_equation: DifferentialEquation, NMAX: int, y_acc) -> Answer:
    if ((differential_equation.b - differential_equation.a) // differential_equation.h) + 1 > NMAX:
        return Answer(None, None, False, "Слишком большое число узлов")

    if ((differential_equation.b - differential_equation.a) / differential_equation.h) + 1 <= 4:
        return modified_euler_method(differential_equation, NMAX, y_acc)

    table =[]
    headers = ["x", "y", "fi", "lambda_fi", "lambda2_fi", "lambda3_fi", "y_acc", "e"]

    h = differential_equation.h
    f = get_function(differential_equation.function_type)
    ans = modified_euler_method(differential_equation, NMAX, y_acc)
    table_runge = ans.table
    if ans.message == "Слишком большой шаг":
        return ans
    x_precalculated = []
    [x_precalculated.append(l[:1][0]) for l in table_runge[:4]]
    y_precalculated = []
    [y_precalculated.append(l[1:2][0]) for l in table_runge[:4]]
    e_precalculated = []
    [e_precalculated.append(l[6:7][0]) for l in table_runge[:4]]

    for i in range(len(x_precalculated)):
        table.append([x_precalculated[i], y_precalculated[i], '', '', '', '', y_acc(x_precalculated[i]), e_precalculated[i]])

    x_curr = x_precalculated[3]
    while x_curr < differential_equation.b:
        try:
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
            table.append([x_curr, y_curr,
                          f(x_precalculated[3], y_precalculated[3]), lambda_fi, lambda2_fi, lambda3_fi, y_acc(x_curr), abs(y_curr - y_acc(x_curr))])
            for i in range(1, 4):
                x_precalculated[i - 1] = x_precalculated[i]
                y_precalculated[i - 1] = y_precalculated[i]
            x_precalculated[3] = x_curr
            y_precalculated[3] = y_curr

            if abs(y_curr - y_acc(x_curr)) > differential_equation.e:
                return Answer(table, headers, False, "Слишком большой шаг")
        except OverflowError:
            return Answer(None, None, False, "Слишком большие числа")

    return Answer(table, headers, True, "")
