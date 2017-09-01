# -*- coding: utf-8 -*-
result = sum(sum(divmod(int(input()), 2)) for _ in range(3))
print(result)
