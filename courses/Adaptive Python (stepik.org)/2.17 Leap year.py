# -*- coding: utf-8 -*-
year = int(input())

print('Leap' if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else 'Regular')