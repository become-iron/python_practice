# -*- coding: utf-8 -*-
# https://stepik.org/lesson/Задачи-41234/step/3?course=Алгоритмы-теория-и-практика-Структуры-данных&unit=19818


def process_packages(size, packages):
    queue = [None] * size
    time = 0
    tail = 0
    process_end = 0
    for arrival, duration in packages:
        if time < arrival:
            time = arrival
        if process_end < time:
            # print(queue)
            del queue[0]
            queue.append(None)
            tail -= 1
            if queue[0] is not None:
                process_end = time + queue[0]
        if queue[-1] is not None:
            # очередь заполнена
            yield -1
        else:
            yield time
            queue[tail] = duration
            tail += 1


if __name__ == '__main__':
    assert tuple(process_packages(1, [[0, 0]])) == (0,)
    print(tuple(process_packages(1, [[0, 1], [0, 1]])))
    assert tuple(process_packages(1, [[0, 1], [0, 1]])) == (0, -1)
    print(tuple(process_packages(1, [[0, 1], [1, 1]])))
    assert tuple(process_packages(1, [[0, 1], [1, 1]])) == (0, 1)
    assert tuple(process_packages(1, [[0, 1]])) == (0,)
    print(tuple(process_packages(1, ((16, 0), (29, 3), (44, 6), (58, 0), (72, 2), (88, 8), (95, 7), (108, 6), (123, 9), (139, 6), (152, 6), (157, 3), (169, 3), (183, 1), (192, 0), (202, 8), (213, 8), (229, 3), (232, 3), (236, 3), (239, 4), (247, 8), (251, 2), (267, 7), (275, 7)))))
    assert \
        tuple(process_packages(1, ((16, 0), (29, 3), (44, 6), (58, 0), (72, 2), (88, 8), (95, 7), (108, 6), (123, 9), (139, 6), (152, 6), (157, 3), (169, 3), (183, 1), (192, 0), (202, 8), (213, 8), (229, 3), (232, 3), (236, 3), (239, 4), (247, 8), (251, 2), (267, 7), (275, 7)))) == \
        (16, 29, 44, 58, 72, 88, -1, 108, 123, 139, 152, -1, 169, 183, 192, 202, 213, 229, 232, 236, 239, 247, -1, 267, 275)
    print(tuple(process_packages(11, ((6, 23), (15, 44), (24, 28), (25, 15), (33, 7), (47, 41), (58, 25), (65, 5), (70, 14), (79, 8), (93, 43), (103, 11), (110, 25), (123, 27), (138, 40), (144, 19), (159, 2), (167, 23), (179, 43), (182, 31), (186, 7), (198, 16), (208, 41), (222, 23), (235, 26)))))
    assert tuple(process_packages(11, ((6, 23), (15, 44), (24, 28), (25, 15), (33, 7), (47, 41), (58, 25), (65, 5), (70, 14), (79, 8), (93, 43), (103, 11), (110, 25), (123, 27), (138, 40), (144, 19), (159, 2), (167, 23), (179, 43), (182, 31), (186, 7), (198, 16), (208, 41), (222, 23), (235, 26)))) == (6, 29, 73, 101, 116, 123, 164, 189, 194, 208, 216, 259, 270, 295, 322, 362, -1, 381, -1, -1, -1, 404, 420, 461, 484)


    # size, n = (int(_) for _ in input().split())
    # for _ in process_packages(size, [[int(_) for _ in input().split(' ')] for _ in range(n)]):
    #     print(_)
