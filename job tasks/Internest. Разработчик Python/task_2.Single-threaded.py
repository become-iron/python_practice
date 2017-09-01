#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import sys
from collections import Counter
from itertools import chain


def count_words():
    file_name = 'words.txt'

    stop_words = set(chain.from_iterable(map(lambda x: x.split(), open(file_name))))

    words = Counter(
        word for word in chain.from_iterable(map(lambda x: x.split(), sys.stdin))
        if word not in stop_words
    )

    for word, amount in words.most_common():
        print '{0} - {1}'.format(word, amount)


if __name__ == '__main__':
    count_words()
