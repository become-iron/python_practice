# -*- coding: utf-8 -*-
A, B, N = (int(input()) for i in range(3))
A = N * A + N * B // 100
B = N * B % 100
print(A, B)
