"""Generators.

生成器 (Generators)

@see: https://www.learnpython.org/en/Generators

Generators are used to create iterators, but with a different approach. Generators are simple
functions which return an iterable set of items, one at a time, in a special way.

生成器用于创建迭代器，但使用了一种不同的方式。生成器是一种简单的函数，它以特殊的方式
一次返回一个可迭代的项集合。

When an iteration over a set of item starts using the for statement, the generator is run. Once the
generator's function code reaches a "yield" statement, the generator yields its execution back to
the for loop, returning a new value from the set. The generator function can generate as many
values (possibly infinite) as it wants, yielding each one in its turn.

当使用 for 语句开始对一组项进行迭代时，生成器会运行。一旦生成器的函数代码到达 "yield"
语句，生成器就会把执行权交还给 for 循环，并从集合中返回一个新的值。生成器函数可以根据需要
生成任意多的值（甚至是无限多），每次轮到它时就产出一个。
"""

import random


def lottery():
    """Generator function example.

    Here is a simple example of a generator function which returns random integers.
    This function decides how to generate the random numbers on its own, and executes the yield
    statements one at a time, pausing in between to yield execution back to the main for loop.
    """
    # 生成器函数示例。
    # 下面是一个生成器函数的简单示例，它返回随机整数。
    # 该函数自己决定如何生成随机数，并一次执行一个 yield 语句，
    # 在两次执行之间暂停，将执行权交还给主 for 循环。

    # returns first 3 random numbers between 1 and 10
    # 返回前 3 个在 1 到 10 之间的随机数
    # pylint: disable=unused-variable
    for i in range(3):
        yield random.randint(1, 10)

    # returns a 4th number between 10 and 20
    # 返回第 4 个在 10 到 20 之间的数
    yield random.randint(10, 20)


def test_generators():
    """Yield statement"""
    # yield 语句
    for number_index, random_number in enumerate(lottery()):
        if number_index < 3:
            assert 0 <= random_number <= 10
        else:
            assert 10 <= random_number <= 20
