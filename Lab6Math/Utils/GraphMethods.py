import matplotlib.pyplot as plt
import numpy as np

from Model.DifferentialEquation import get_acc_function, DifferentialEquation, acc_function_arr


def draw_graph(table_ans: list, differential_equation: DifferentialEquation):
    plt.cla()
    plt.clf()
    plt.gcf().canvas.set_window_title("График интерполяций")
    plt.grid()
    axes = plt.gca()

    axes.spines['right'].set_color('none')
    axes.spines['top'].set_color('none')
    axes.spines['left'].set_position('zero')
    axes.spines['bottom'].set_position('zero')
    axes.set_xlabel('x', loc='right')
    axes.set_ylabel('y', loc='top')
    axes.plot(1, 0, marker=">", ms=5, color='k', transform=axes.get_yaxis_transform(), clip_on=False)
    axes.plot(0, 1, marker="^", ms=5, color='k', transform=axes.get_xaxis_transform(), clip_on=False)

    # точное решение
    X = np.linspace(differential_equation.a - 0.2, differential_equation.b + 0.2, 100)
    F = get_acc_function(differential_equation.function_type)
    axes.plot(X, F(X), label=acc_function_arr[differential_equation.function_type])

    # таблица полученная от метода
    x_arr = []
    y_arr = []
    for i in range(len(table_ans)):
        x_arr.append(table_ans[i][0])
        y_arr.append(table_ans[i][1])

    axes.plot(x_arr, y_arr, label="y(x)")

    axes.legend()
    plt.savefig("graph")
