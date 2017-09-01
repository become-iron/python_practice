# -*- coding: utf-8 -*-
# https://stepik.org/lesson/Задачи-41560/step/1?course=Алгоритмы-теория-и-практика-Структуры-данных&unit=20013


class MinHeap:
    def __init__(self, array):
        self.heap = list(array)
        self.log = []
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
                self.log.append((i, min_i))
                self.heap[i], self.heap[min_i] = self.heap[min_i], self.heap[i]
                i = min_i
            else:
                break


if __name__ == '__main__':
    # heap = MinHeap([5, 4, 3, 2, 1])
    # print(heap.heap)
    # print(*heap.log, sep='\n')
    # heap = MinHeap([1, 2, 3, 4, 5])
    # print(heap.heap)

    input()
    heap = MinHeap(list(map(int, input().split())))
    print(len(heap.log))
    for item in heap.log:
        print(*item)
