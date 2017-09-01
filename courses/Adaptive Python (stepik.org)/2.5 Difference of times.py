# -*- coding: utf-8 -*-
fh, fm, fs, sh, sm, ss = (int(input()) for i in range(6))

result = (sh - fh) * 3600 + (sm - fm) * 60 + (ss - fs)

print(result)

