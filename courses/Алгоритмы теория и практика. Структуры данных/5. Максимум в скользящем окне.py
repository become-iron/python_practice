# -*- coding: utf-8 -*-


# def max_in_window(arr, size):
#     if size == 1:
#         yield from arr
#         return
#     for i in range(len(arr) - size + 1):
#         max_ = max(arr[i + 1: i + size])
#         last_max = arr[i] if arr[i] > max_ else max_
#         yield last_max


# def max_in_window(arr, size):
#     if size == 1:
#         yield from arr
#         return
#     maxs = [max(arr[i: i + 2]) for i in range(size - 1)]
#     yield max(maxs)
#     del arr[:size-1]
#     for i in range(len(arr)-1):
#         del maxs[0]
#         maxs.append(max(arr[0: 2]))
#         del arr[0]
#         yield max(maxs)

# from collections import deque
# def max_in_window(arr, size):
#     if size == 1:
#         yield from arr
#         return
#     queue = deque(arr[:size-1], size)
#     for i in range(size - 1, len(arr)):
#         queue.append(arr[i])
#         yield max(queue)

# def max_in_window(arr, size):
#     if size == 1:
#         yield from arr
#         return
#     yield from (max(arr[i: i + size]) for i in range(len(arr) - size + 1))

def max_in_window(arr, size):
    if size == 1:
        yield from arr
        return
    else:
        for i in range(len(arr) - size + 1):
            yield max(arr[i: i + size])

if __name__ == '__main__':
    print(list(max_in_window([2, 7, 3, 1, 5, 2, 6, 2], 4)))
    assert list(max_in_window([2, 7, 3, 1, 5, 2, 6, 2], 4)) == [7, 7, 5, 6, 6]
    assert list(max_in_window([2, 1, 5], 1)) == [2, 1, 5]
    assert list(max_in_window([2, 3, 9], 3)) == [9]

    assert list(max_in_window([2, 1, 5], 2)) == [2, 5]

    # для ввода при тестировании на сайте
    # input()
    # print(*max_in_window(list(int(i) for i in input().split()), int(input())))
