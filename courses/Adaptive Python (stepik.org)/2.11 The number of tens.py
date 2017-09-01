# -*- coding: utf-8 -*-
try:
    result = input()[-2]
except IndexError:
    result = 0

print(result)
