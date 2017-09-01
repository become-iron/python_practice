# -*- coding: utf-8 -*-
a, b, c = (int(input()) for _ in range(3))

print(
    'YES'
    if ((a > 0) and (b > 0) and (c > 0) and (a + b > c) and (b + c > a) and (c + a > b))
    else 'NO'
)
