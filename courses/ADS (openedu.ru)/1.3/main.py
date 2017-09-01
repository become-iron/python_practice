# -*- coding: utf-8 -*-

# Сортировка вставками

with open('input.txt') as in_file:
    amount = int(in_file.readline())
    nums = list(map(float, in_file.readline().split()))

positions = [1]

for j in range(1, len(nums)):
    i = j - 1
    while i >= 0 and nums[i] > nums[i+1]:
        nums[i], nums[i+1] = nums[i+1], nums[i]
        i -= 1
    positions.append(i + 2)

with open('output.txt', 'w') as out_file:
    out_file.write(' '.join(map(str, positions)))
    out_file.write('\n')
    out_file.write(' '.join(map(str, nums)))
