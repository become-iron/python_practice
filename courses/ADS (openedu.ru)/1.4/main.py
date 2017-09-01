# -*- coding: utf-8 -*-

# Знакомство с жителями Сортлэнда

with open('input.txt') as in_file:
    amount = int(in_file.readline())
    nums = list(map(int, in_file.readline().split()))

tmp = tuple(sorted(enumerate(nums), key=lambda x: x[1]))

result = (tmp[0][0], tmp[amount // 2][0], tmp[-1][0])

with open('output.txt', 'w') as out_file:
    out_file.write(' '.join(map(lambda x: str(x+1), result)))
