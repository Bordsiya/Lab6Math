from Methods.MethodsUtils import do_method, calculate_final_table_with_accuracy
from Utils.GraphMethods import draw_graph
from Utils.IOMethods import get_data, get_method, print_table

differential_equation = get_data()
#print("//", differential_equation_h)
method_id = get_method()
table, headers = calculate_final_table_with_accuracy(method_id, differential_equation)
if table is not None:
    draw_graph(table, differential_equation)
