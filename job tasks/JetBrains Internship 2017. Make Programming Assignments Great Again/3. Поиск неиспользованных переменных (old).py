
# обход в глубину, с системой детекции использования переменной
# def find_unused_vars(code):
#     def process_node(node, using):
#         if isinstance(node, (list, tuple)):
#             for _node in node:
#                 process_node(_node, using)
#         elif isinstance(node, ast.Name):  # именованный объект
#             # print(ast.dump(node), using)
#             if using:
#                 used.add(node.id)
#                 if node.id in used:  # если переменная была определена ранее
#                     used.remove(node.id)
#             else:
#                 declared.add(node.id)
#         elif isinstance(node, ast.Expr):  # выражение
#             # print(ast.dump(node))
#             process_node(node.value, True)
#         elif isinstance(node, ast.Assign):  # присваивание
#             process_node(node.targets, False)
#             process_node(node.value, True)
#         elif isinstance(node, ast.UnaryOp):  # унарная операция
#             process_node(node.operand, using)
#         elif isinstance(node, ast.BinOp):  # бинарная операция
#             process_node(node.left, True)
#             process_node(node.right, True)
#         elif isinstance(node, ast.BoolOp):  # логическая операция
#             for _node in node.values:
#                 process_node(_node, False)
#         elif isinstance(node, ast.AugAssign):  # составное присваивание
#             process_node(node.target, False)  # TODO: может, и нет смысла обрабатывать
#             process_node(node.value, True)
#         elif isinstance(node, ast.Compare):  # операция сравнения
#             process_node(node.left, True)
#             for _node in node.comparators:
#                 process_node(_node, True)
#         elif isinstance(node, ast.Delete):  # удаление
#             for _node in node.targets:
#                 process_node(_node, True)
#         elif isinstance(node, ast.Call):  # вызов (функции, класса)
#             process_node(node.func, True)
#             for _node in node.args:
#                 process_node(_node, True)
#             for _node in node.keywords:
#                 process_node(_node, True)
#         elif isinstance(node, ast.Attribute):  # доступ к свойству или методу
#             process_node(node.value, True)
#         elif isinstance(node, ast.keyword):  # именованный аргумент
#             process_node(node.value, True)
#         elif isinstance(node, (ast.Tuple, ast.List, ast.Set)):  # список/кортеж/множество
#             for _node in node.elts:
#                 process_node(_node, using)
#             # TODO keywords
#         elif isinstance(node, ast.Dict):  # словарь
#             for _node in node.keys:
#                 process_node(_node, True)
#             for _node in node.values:
#                 process_node(_node, True)
#         elif isinstance(node, ast.If):  # условие
#             process_node(node.test, True)
#             if hasattr(node, 'comparators'):
#                 for _node in node.comparators:
#                     process_node(_node, True)
#             for _node in node.body:
#                 process_node(_node, False)
#             for _node in node.orelse:
#                 process_node(_node, False)
#         elif isinstance(node, ast.IfExp):  # тернарный оператор
#             process_node(node.test, True)
#             process_node(node.body, using)
#             process_node(node.orelse, using)
#         elif isinstance(node, ast.Subscript):  # взятие по индексу или срезу
#             process_node(node.value, True)
#             process_node(node.slice, True)
#         elif isinstance(node, ast.Index):  # индекс
#             process_node(node.value, True)
#         elif isinstance(node, ast.Slice):  # срез
#             process_node(node.lower, True)
#             process_node(node.upper, True)
#             if node.step is not None:
#                 process_node(node.step, True)
#         elif isinstance(node, ast.For):  # цикл for
#             process_node(node.target, False)
#             process_node(node.iter, True)
#             for _node in node.body:
#                 process_node(_node, False)
#             for _node in node.orelse:
#                 process_node(_node, False)
#         elif isinstance(node, ast.While):  # цикл while
#             process_node(node.test, True)
#             for _node in node.body:
#                 process_node(_node, False)
#             for _node in node.orelse:
#                 process_node(_node, False)
#         elif isinstance(node, ast.With):  # оператор with
#             for _node in node.items:  # withitem
#                 process_node(_node.context_expr, True)
#                 process_node(_node.optional_vars, False)
#             for _node in node.body:
#                 process_node(_node, False)
#         else:
#             try:  # для совместимости с Python < 3.6
#                 if isinstance(node, ast.FormattedValue):  # форматированная строка
#                     process_node(node.value, True)
#                     return
#             except AttributeError:
#                 pass
#             # print(ast.dump(node))
#
#     declared = set()  # объявленные переменные
#     used = set()  # использованные переменные
#     tree = ast.parse(code)
#     for subtree in tree.body:
#         process_node(subtree, False)
#     # print(declared, used, declared - used)
#     return tuple(declared - used)


# обход в ширину, с использованием метаданных
# def find_unused_vars(code):
#     declared = set()  # имена объявленных объектов
#     used = set()  # имена использованных объектов
#     for node in ast.walk(ast.parse(code)):  # рекурсивно проходим по всем узлам
#         if isinstance(node, ast.Name):  # если именованный объект (переменные, функции, классы)
#             # присваивается новое значение
#             if isinstance(node.ctx, ast.Store):  # ctx = Store()
#                 declared.add(node.id)
#                 if node.id in used:  # если переменная была определена ранее
#                     used.remove(node.id)
#             # загружается или удаляется
#             else:  # ctx = Load() or ctx = Del()
#                 used.add(node.id)
#     return declared - used
