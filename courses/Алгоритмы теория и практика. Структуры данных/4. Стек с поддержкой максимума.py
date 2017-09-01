# -*- coding: utf-8 -*-


def stack_(*commands):
    stack = [0] * 1048576
    max_stack = [0] * 1048576
    last_n = 0
    last_max = 0
    for command in commands:
        if command.startswith('po'):  # pop
            stack[last_n] = 0
            max_stack[last_n] = 0
            last_n -= 1
            last_max = max_stack[last_n]
        elif command.startswith('m'):  # max
            yield last_max
        else:  # push
            last_n += 1
            value = int(command.split(' ')[1])
            stack[last_n] = value
            if value > last_max:
                max_stack[last_n] = value
                last_max = value
            else:
                max_stack[last_n] = last_max

if __name__ == '__main__':
    assert tuple(stack_('push 2', 'push 1', 'max', 'pop', 'max')) == (2, 2)
    # print(tuple(stack_('push 1', 'push 2', 'max', 'pop', 'max')))
    assert tuple(stack_('push 1', 'push 2', 'max', 'pop', 'max')) == (2, 1)
    assert tuple(stack_('push 2', 'push 3', 'push 9', 'push 7', 'push 2', 'max', 'max', 'max', 'pop', 'max')) ==\
           (9, 9, 9, 9)
    #
    # for i in range(int(input())):
    #     command = input()

    # stack = [0] * 65536
    # max_stack = [0] * 65536
    # last_n = 0
    # last_max = 0
    # for i in range(int(input())):
    #     command = input()
    #     if command.startswith('po'):  # pop
    #         stack[last_n] = 0
    #         max_stack[last_n] = 0
    #         last_n -= 1
    #         last_max = max_stack[last_n]
    #     elif command.startswith('m'):  # max
    #         print(last_max)
    #     else:  # push
    #         value = int(command.split(' ')[1])
    #         stack[last_n] = value
    #         if value > last_max:
    #             max_stack[last_n] = value
    #             last_max = value
    #         else:
    #             max_stack[last_n] = last_max
