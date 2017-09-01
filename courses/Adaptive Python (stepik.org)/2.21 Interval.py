# -*- coding: utf-8 -*-


def check(num):
    if -15 < num <= 12:
        return True
    elif 14 < num < 17:
        return True
    elif 19 <= num:
        return True
    return False

print(check(int(input())))


# print((lambda x: -15 < x <= 12 or 14 < x < 17 or 19 <= x)(int(input())))
