from Methods.MethodsUtils import do_method, calculate_final_table_with_accuracy
from Utils.GraphMethods import draw_graph
from Utils.IOMethods import get_data, get_method, print_table

differential_equation_h = get_data()
method_id = get_method()
table_h, headers_h = do_method(method_id, differential_equation_h)
table_h, headers_h = calculate_final_table_with_accuracy(method_id, differential_equation_h, table_h, headers_h)
print_table(table_h, headers_h)
draw_graph(table_h, differential_equation_h)
