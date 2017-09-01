# -*- coding: utf-8 -*-
# https://stepik.org/lesson/Задачи-41234/step/2?unit=19818


def get_tree_height(n, tree):
    tree = tuple(map(int, tree.split(' ')))
    node_heights = dict()
    height = 0

    for node in tree:
        tmp_node = node
        tmp_height = 1
        while True:
            if tmp_node == -1:
                break
            tmp_node = tree[tmp_node]
            cached_node_height = node_heights.get(tmp_node, None)
            if cached_node_height is not None:
                tmp_height += cached_node_height
                break
            tmp_height += 1
        if node_heights.get(node, None) is None:
            node_heights[node] = tmp_height
        if tmp_height > height:
            height = tmp_height
    return height


if __name__ == '__main__':
    assert get_tree_height('5', '4 -1 4 1 1') == 3, 'meow'
    assert get_tree_height('5', '-1 0 4 0 3') == 4
    assert get_tree_height('10', '9 7 5 5 2 9 9 9 2 -1') == 4

    assert get_tree_height('1', '-1') == 1
    assert get_tree_height('2', '-1 0') == 2
    assert get_tree_height('3', '1 2 -1') == 3
    assert get_tree_height('3', '-1 0 0') == 2

    # print(get_tree_height(input(), input()))
