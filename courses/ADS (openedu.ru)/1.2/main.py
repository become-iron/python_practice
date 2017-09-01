# -*- coding: utf-8 -*-

with open('input.txt', 'r') as in_file:
    with open('output.txt', 'w') as out_file:
        nums = tuple(map(int, in_file.read().split()))
        result = nums[0] + nums[1] ** 2
        out_file.write(str(result))
