# -*- coding: utf-8 -*-
# https://stepik.org/lesson/Задачи-41234/step/1?unit=19818


def put_brackets(string):
    brackets = []
    last = None

    for i, sym in enumerate(string):
        if sym in ('(', '{', '['):
            last = ({'(': ')', '{': '}', '[': ']'}[sym], i)
            brackets.append(last)

        elif sym in (')', '}', ']'):
            if last is None or sym != last[0]:
                # не было открывающей или неожиданная закрывающая скобка
                return i + 1
            else:
                # ожидаемая закрывающая скобка
                del brackets[-1]
                last = brackets[-1] if brackets else None
    if brackets:
        return brackets[-1][1] + 1
    return 'Success'

if __name__ == '__main__':
    assert put_brackets('[]') == 'Success'
    assert put_brackets('{}[]') == 'Success'
    assert put_brackets('[()]') == 'Success'
    assert put_brackets('(())') == 'Success'
    assert put_brackets('{[]}()') == 'Success'
    assert put_brackets('{') == 1
    assert put_brackets('{[}') == 3
    assert put_brackets('foo(bar);') == 'Success'
    assert put_brackets('foo(bar[i);') == 10

# if __name__ == '__main__':
#     print(put_brackets(input()))
