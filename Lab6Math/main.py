from Methods.MethodsUtils import do_method
from Utils.GraphMethods import draw_graph
from Utils.IOMethods import get_data, get_method, print_table

differential_equation = get_data()
method_id = get_method()
table, headers = do_method(method_id, differential_equation)
print_table(table, headers)
draw_graph(table, differential_equation)
