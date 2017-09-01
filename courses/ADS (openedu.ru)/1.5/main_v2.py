# -*- coding: utf-8 -*-

# Секретарь Своп

# !не верно!

with open('input.txt') as in_file:
    amount = int(in_file.readline())
    nums = tuple(map(int, in_file.readline().split()))

with open('output.txt', 'w') as out_file:
    for i, item in enumerate(sorted(enumerate(nums), key=lambda x: x[1])):
        out_file.write('Swap elements at indices {} and {}.\n'.format(item[0] + 1, i + 1))
    out_file.write('No more swaps needed.\n')
    out_file.write(' '.join(map(str, sorted(nums))))
