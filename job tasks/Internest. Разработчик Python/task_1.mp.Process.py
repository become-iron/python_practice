#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import sys
import multiprocessing as mp
from itertools import chain


def process_line(in_queue, out_dict):
    while True:
        line = in_queue.get()
        if line is None:
            return

        for word in line.split():
            try:
                out_dict[word] += 1
            except KeyError:
                out_dict[word] = 1


def count_words():
    num_procs = mp.cpu_count()

    with mp.Manager() as manager:
        data_queue = manager.Queue()
        results = manager.dict()

        pool = []
        for i in xrange(num_procs):
            p = mp.Process(target=process_line, args=(data_queue, results))
            pool.append(p)
            p.start()

        for line in chain(sys.stdin, (None,) * num_procs):
            data_queue.put(line)

        # for p in pool:
        #     p.join()

        for word, amount in sorted(results.items(), key=lambda x: (x[1], x[0]), reverse=True):
            print '{0} - {1}'.format(word, amount)


if __name__ == '__main__':
    count_words()
