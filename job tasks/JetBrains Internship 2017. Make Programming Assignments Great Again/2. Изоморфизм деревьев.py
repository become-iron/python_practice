# -*- coding: utf-8 -*-
"""Изоморфизм деревьев. Два бинарных дерева заданы как списки номеров родительских вершин."""


def isomorphic(tree, tree2):
    """Проверка деревьев на изоморфизм"""
    def check_node(first, second):
        if first == second == [None, None]:  # оба узла - листья
            return True
        elif all(_[0] is not None and _[1] is None for _ in (first, second)):  # оба имеют одного потомка
            return check_node(tree[first[0]], tree2[second[0]])
        elif all(_[0] is not None and _[1] is not None for _ in (first, second)):  # оба имеют двух потомков
            # левые потомки узлов и правые потомки узлов
            # или
            # (левый потомок первого узла и правый второго) и (правый потомок первого узла и левый второго)
            return (check_node(tree[first[0]], tree2[second[0]]) and
                    check_node(tree[first[1]], tree2[second[1]])) or \
                   (check_node(tree[first[0]], tree2[second[1]]) and
                    check_node(tree[first[1]], tree2[second[0]]))
        else:  # (один - лист, другой - нет) или (один имеет одного потомка, другой - двух)
            return False

    if not tree and not tree2:  # оба дерева - пустые
        return True
    elif (not tree and tree2) or (tree and not tree2):  # одно из деревьев - пустое, другое - нет
        return False
    return check_node(tree[tree[-1]], tree2[tree2[-1]])


def make_tree(array):
    """Оформление дерева в удобный для работы формат"""
    tree = [[None, None] for _ in range(len(array))]
    for node, parent in enumerate(array):
        # узел: [потомок 1, потомок 2]
        # работа с родителем узла
        if parent == -1 or parent == node:  # если корень
            tree.append(node)  # добавляем индекс корня в конец списка
            continue
        if tree[parent][0] is None:  # первый потомок не определён
            tree[parent] = [node, None]
        else:
            tree[parent][1] = node
    return tree


if __name__ == '__main__':
    # print(make_tree([2, 2, -1]))
    # print(make_tree([1, -1, 1]))
    assert isomorphic(make_tree([2, 2, -1]), make_tree([1, -1, 1])) is True
    assert isomorphic(make_tree([-1, 0, 1]), make_tree([1, -1, 1])) is False

    assert isomorphic(make_tree([-1]), make_tree([-1])) is True
    assert isomorphic(make_tree([-1]), make_tree([-1, 0])) is False
    assert isomorphic(make_tree([2, 2, -1]), make_tree([2, 2, -1])) is True
    assert isomorphic(make_tree([-1, 0, 0, 1, 1]), make_tree([-1, 0, 0, 2, 2])) is True
    assert isomorphic(make_tree([0, 0, 0, 1, 1]), make_tree([0, 0, 0, 2, 2])) is True
    assert isomorphic(make_tree([-1, 0, 0, 1, 1]), make_tree([-1, 0, 0, 1, 2])) is False
    assert isomorphic(make_tree([-1, 0, 0, 1, 3]), make_tree([-1, 0, 0, 2, 3])) is True
    assert isomorphic(make_tree([-1, 0, 0, 1, 3]), make_tree([])) is False
    assert isomorphic(make_tree([]), make_tree([])) is True

# input()
# print('YES' if isomorphic(*(make_tree(list(map(int, input().split()))) for _ in range(2))) else 'NO')
