# -*- coding: utf-8 -*-
time = int(input())
h, m, s = (time // 3600 % 24, time % 3600 // 60, time % 3600 % 60)
print('{}:{:02}:{:02}'.format(h, m, s))

