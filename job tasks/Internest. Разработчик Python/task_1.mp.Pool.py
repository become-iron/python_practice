#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import sys
import multiprocessing.dummy as mp
from collections import Counter
from itertools import chain


def process_line(line):
    return line.split()


def count_words():
    num_procs = mp.cpu_count()

    pool = mp.Pool(num_procs)
    results = Counter(chain.from_iterable(pool.map(process_line, sys.stdin)))
    pool.close()

    for word, amount in results.most_common():
        print '{0} - {1}'.format(word, amount)


if __name__ == '__main__':
    count_words()
