# -*- coding: utf-8 -*-
with open('input.txt', 'r') as in_file:
    with open('output.txt', 'w') as out_file:
        out_file.write(str(sum(tuple(map(int, in_file.read().split())))))
