# -*- coding: utf-8 -*-
"""
Дан простой скрипт на Python 3, использующий только самые базовые конструкции языка. В скрипте нет определений функций 
и классов, нет list comprehensions, generator expression и т.п.
Найдите переменные, которые в коде определены, но не используются после присвоения им значения. 
Выведите названия переменных в любом порядке.
"""

import ast


# обход в глубину, с использованием метаданных
def find_unused_vars(code):
    class DepthFirstWalk(ast.NodeVisitor):
        def visit_Name(self, node):  # если именованный объект (переменные, функции, классы)
            var_name = node.id
            # присваивается новое значение
            if isinstance(node.ctx, ast.Store):  # ctx = Store()
                # если переменная была объявлена ранее, но не использовалась
                # if var_name in declared and var_name not in used:
                #     pass

                # если переменная была определена ранее и использовалась
                if var_name in used:
                    used.remove(var_name)
                declared.add(var_name)
            # загружается или удаляется
            else:  # ctx = Load() or ctx = Del()
                used.add(var_name)

    declared = set()  # имена объявленных объектов
    used = set()  # имена использованных объектов
    tree = ast.parse(code)  # разбор в AST-дерево
    DepthFirstWalk().visit(tree)
    return declared - used


# noinspection SqlDialectInspection,SqlNoDataSourceInspection
tests = [
["""a = 2
b = 3
c = a""", {'c', 'b'}],

["""a = 2
b = 3
c = "Hello"
x = a + b
x = a
print(a)
for i in range(10):
  print(a)""", {'x', 'c', 'i'}],

["""a = 1
a += 1""", {'a'}],

["""a = []
a.append(3)""", set()],

["""x = 0
if x < 2:
    pass""", set()],

["""a = 1
b = 2
a = a + b
b = a + b""", set()],

["""
a = 1
b = 2
print(b)""", {'a'}],

["""a = 0
a += 1""", {'a'}],

["""a = 2
a = 3
b = a""", {'b'}],

["""a = []
a.append(3)""", set()],

["""a = 1
b = 2
c = 2
if a == b:
    d = 1
    for i in c:
        a = d""", {'i', 'a'}],

["""a = 2
b = 3
c = "Hello"
x = a + b
x = a
print(a)
for i in range(10):
  print(a)""", {'i', 'x', 'c'}],

["""a = 1
for _ in range(int(input())):
    a = a + a""", set('_')],

["""qwerty = 56""", {'qwerty'}],

["""a = 12
print(a)
b = 3
a[b]
c = 12
for _ in range(a):
    if b in _:
        g = 23
        g /= c""", {'g'}],

["""a = 23
b = c = d = a""", {'b', 'c', 'd'}],

["""a = 1
b = 2
a, b = b, a""", set()],

["""a = 23
while a == 23:
    b = c = 23
    b *= 12
    print(c)""", {'b'}],

["""for i in range(12):
    pass""", {'i'}],

["""with open('a.txt') as file:
  print(file.read)""", set()],

["""a = 12
f'{a}'""", set()],

["""a = 'meow'
a.__repr__""", set()],

["""a = 1
a = a + 1""", set()],

["""a = 1
if True:
    if not None:
        b = 1
        if b:
            for i in range(b):
                a""", {'i'}],

["""a = something()
a(123)""", set()],

["""a = 23
for i, b in a:
    print(i)""", {'b'}],

# c переносом с помощью слеша
["""a = \\
    12""", {'a'}],

["""a = 3
b = a
a = 2""", {'a', 'b'}],

# ["""""", set()],
# ["""""", set()],
]


for code, expected_result in tests:
    result = set(find_unused_vars(code))
    # print(ast.dump(ast.parse(code)))
    try:
        assert result == expected_result
    except AssertionError:
        print(code, expected_result, result, sep='\n')
        raise


# import sys
# _ = find_unused_vars(sys.stdin.read())
# if _:
#     print(*_, sep='\n')


# path = r"D:\Python\become-iron\vsptd\vsptd\extra.py"
# print(*find_unused_vars(open(path, encoding='utf-8').read()), sep='\n')

