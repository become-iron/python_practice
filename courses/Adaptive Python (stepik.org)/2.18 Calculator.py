# -*- coding: utf-8 -*-
n1, n2, op = (float(input()), float(input()), input())

result = None

if op == '+':
    result = n1 + n2
elif op == '-':
    result = n1 - n2
elif op == '/':
    if n2 == 0:
        result = 'Division by 0!'
    else:
        result = n1 / n2
elif op == '*':
    result = n1 * n2
elif op == 'mod':
    if n2 == 0:
        result = 'Division by 0!'
    else:
        result = n1 % n2
elif op == 'pow':
    result = n1 ** n2
elif op == 'div':
    if n2 == 0:
        result = 'Division by 0!'
    else:
        result = n1 // n2

print(result)
