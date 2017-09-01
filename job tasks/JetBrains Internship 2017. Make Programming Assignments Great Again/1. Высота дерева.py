# -*- coding: utf-8 -*-
"""Высота дерева. Дерево задано как список номеров родительских вершин (нумерация с 0)."""


def get_tree_height(n, tree):
    n = int(n)
    tree = tuple(map(int, tree.split(' ')))
    subtree_depths = [None] * n
    height = 0

    for child, parent in enumerate(tree):
        subtree_depth = 1
        cur_child, cur_parent = child, parent
        while cur_parent != -1:  # поднимаемся до корня
            cur_child, cur_parent = cur_parent, tree[cur_parent]
            if subtree_depths[cur_child] is not None:  # глубина узла кэширована ранее
                subtree_depth += subtree_depths[cur_child]
                break
            subtree_depth += 1
        if subtree_depths[child] is None:  # кэшируем глубину узла
            subtree_depths[child] = subtree_depth
        if subtree_depth > height:
            height = subtree_depth

    return height


if __name__ == '__main__':
    # print(get_tree_height('5', '4 -1 4 1 1'))
    assert get_tree_height('5', '4 -1 4 1 1') == 3
    assert get_tree_height('5', '-1 0 4 0 3') == 4
    assert get_tree_height('10', '9 7 5 5 2 9 9 9 2 -1') == 4

    assert get_tree_height('1', '-1') == 1
    assert get_tree_height('2', '-1 0') == 2
    assert get_tree_height('3', '1 2 -1') == 3
    assert get_tree_height('3', '-1 0 0') == 2

    # print(get_tree_height(input(), input()))
