# -*- coding: utf-8 -*-

# Секретарь Своп

# !не прошло по времени!

with open('input.txt') as in_file:
    amount = int(in_file.readline())
    nums = list(map(int, in_file.readline().split()))

with open('output.txt', 'w') as out_file:
    for j in range(1, amount):
        i = j - 1
        while i >= 0 and nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            out_file.write('Swap elements at indices {} and {}.\n'.format(i + 1, i + 2))
            i -= 1
    out_file.write('No more swaps needed.\n')
    out_file.write(' '.join(map(str, nums)))
