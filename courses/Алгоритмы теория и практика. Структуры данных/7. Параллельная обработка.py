# -*- coding: utf-8 -*-
from math import log2, ceil as round_up


class MinHeap:
    # parent = round_down((i - 1) / 2)
    # left_child = 2 * i + 1
    # right_child = 2 * i + 2
    def __init__(self, array):
        self.heap = list(array)
        for i in range(int(self.size / 2), -1, -1):
            self.sift_down(i)

    @property
    def size(self):
        return len(self.heap)

    def sift_down(self, i):
        while True:
            min_i = i
            l = 2 * i + 1
            r = 2 * i + 2
            if l < self.size and self.heap[l] < self.heap[min_i]:
                min_i = l
            if r < self.size and self.heap[r] < self.heap[min_i]:
                min_i = r
            if min_i != i:
                self.heap[i], self.heap[min_i] = self.heap[min_i], self.heap[i]
                i = min_i
            else:
                break


def process_queue(n, queue):
    heap = MinHeap([(0, p_n) for p_n in range(n)])  # (время освобождения, номер процессора)
    for task_time in queue:
        _ = heap.heap[0]
        print(_[1], _[0])
        _ = (_[0] + task_time, _[1])
        heap.heap[0] = _
        heap.sift_down(0)


if __name__ == '__main__':
    process_queue(2, [1, 2, 3, 4, 5])
    process_queue(4, [1] * 20)

    # n = int(input())
    # input()
    # process_queue(n, map(int, input().split()))
