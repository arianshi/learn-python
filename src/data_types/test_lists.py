"""Lists.

# @see: https://www.learnpython.org/en/Lists
# @see: https://docs.python.org/3/tutorial/introduction.html
# @ee: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists

Python knows a number of compound data types, used to group together
other values. The most versatile is the list, which can be written as a
list of comma-separated values (items) between square brackets. Lists
might contain items of different types, but usually the items all have
the same type.
"""

import pytest


def test_list_type():
    """List type."""

    # Lists are very similar to arrays. They can contain any type of variable, and they can contain
    # as many variables as you wish. Lists can also be iterated over in a very simple manner.
    # Here is an example of how to build a list.
    # 列表与数组非常相似，可以包含任意类型的变量，数量不限，也可以非常简便地进行迭代。
    # 下面是一个创建列表的示例。
    squares = [1, 4, 9, 16, 25]

    assert isinstance(squares, list)

    """"
       | 1 |  4 |  9 | 16 | 25
       | 0 |  1 |  2 |  3 |  4
       |-5 | -4 | -3 | -2 | -1

    """
    # Like strings (and all other built-in sequence type), lists can be
    # indexed and sliced:
    # 与字符串（及所有其他内置序列类型）一样，列表可以被索引和切片。
    assert squares[0] == 1  # indexing returns the item
    assert squares[-1] == 25
    assert squares[-3:] == [9, 16, 25]  # slicing returns a new list

    # All slice operations return a new list containing the requested elements.
    # This means that the following slice returns a new (shallow) copy of
    # the list:
    # 所有切片操作都返回一个包含所请求元素的新列表，因此下面的切片返回的是列表的一个新的（浅）拷贝。
    assert squares[:] == [1, 4, 9, 16, 25]

    # Lists also support operations like concatenation:
    # 列表也支持拼接等操作。
    assert squares + [36, 49, 64, 81, 100] == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    # IMPORTANT: Unlike strings, which are immutable, lists are a mutable type, i.e. it
    # is possible to change their content:
    # 重要提示：与不可变的字符串不同，列表是可变类型，即可以修改其内容。
    cubes = [1, 8, 27, 65, 125]  # something's wrong here, the cube of 4 is 64!
    cubes[3] = 64  # replace the wrong value
    assert cubes == [1, 8, 27, 64, 125]

    # You can also add new items at the end of the list, by using
    # the append() method
    # 也可以使用 append() 方法在列表末尾添加新元素。
    cubes.append(216)  # add the cube of 6
    cubes.append(7 ** 3)  # and the cube of 7
    assert cubes == [1, 8, 27, 64, 125, 216, 343]

    # Assignment to slices is also possible, and this can even change the size
    # of the list or clear it entirely:
    # 也可以对切片赋值，这甚至可以改变列表的大小或清空整个列表。
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    letters[2:5] = ['C', 'D', 'E']  # replace some values
    assert letters == ['a', 'b', 'C', 'D', 'E', 'f', 'g']
    letters[2:5] = []  # now remove them
    assert letters == ['a', 'b', 'f', 'g']
    # clear the list by replacing all the elements with an empty list
    # 用空列表替换所有元素，从而清空列表。
    letters[:] = []
    assert letters == []

    # The built-in function len() also applies to lists
    # 内置函数 len() 同样适用于列表。
    letters = ['a', 'b', 'c', 'd']
    assert len(letters) == 4

    # It is possible to nest lists (create lists containing other lists),
    # for example:
    # 可以嵌套列表（即创建包含其他列表的列表），例如：
    list_of_chars = ['a', 'b', 'c']
    list_of_numbers = [1, 2, 3]
    mixed_list = [list_of_chars, list_of_numbers]
    assert mixed_list == [['a', 'b', 'c'], [1, 2, 3]]
    assert mixed_list[0] == ['a', 'b', 'c']
    assert mixed_list[0][1] == 'b'


def test_list_methods():
    """Test list methods."""

    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

    # list.append(x)
    # Add an item to the end of the list.
    # Equivalent to a[len(a):] = [x].
    # 将元素添加到列表末尾，等价于 a[len(a):] = [x]。
    fruits.append('grape')
    assert fruits == ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'grape']

    # list.remove(x)
    # Remove the first item from the list whose value is equal to x.
    # It raises a ValueError if there is no such item.
    # 删除列表中第一个值等于 x 的元素，如果不存在则抛出 ValueError。
    fruits.remove('grape')
    assert fruits == ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

    with pytest.raises(Exception):
        fruits.remove('not existing element')

    # list.insert(i, x)
    # Insert an item at a given position. The first argument is the index of the element
    # before which to insert, so a.insert(0, x) inserts at the front of the list,
    # and a.insert(len(a), x) is equivalent to a.append(x).
    # 在指定位置插入元素。第一个参数是插入位置前的元素索引，a.insert(0, x) 在列表头部插入，
    # a.insert(len(a), x) 等价于 a.append(x)。
    fruits.insert(0, 'grape')
    assert fruits == ['grape', 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

    # list.index(x[, start[, end]])
    # Return zero-based index in the list of the first item whose value is equal to x.
    # Raises a ValueError if there is no such item.
    # The optional arguments start and end are interpreted as in the slice notation and are used
    # to limit the search to a particular subsequence of the list. The returned index is computed
    # relative to the beginning of the full sequence rather than the start argument.
    # 返回列表中第一个值等于 x 的元素的从零开始的索引，不存在则抛出 ValueError。
    # 可选参数 start 和 end 与切片表示法相同，用于限定搜索范围，返回的索引相对于整个序列的起始位置。
    assert fruits.index('grape') == 0
    assert fruits.index('orange') == 1
    assert fruits.index('banana') == 4
    assert fruits.index('banana', 5) == 7  # Find next banana starting a position 5

    with pytest.raises(Exception):
        fruits.index('not existing element')

    # list.count(x)
    # Return the number of times x appears in the list.
    # 返回 x 在列表中出现的次数。
    assert fruits.count('tangerine') == 0
    assert fruits.count('banana') == 2

    # list.copy()
    # Return a shallow copy of the list. Equivalent to a[:].
    # 返回列表的浅拷贝，等价于 a[:]。
    fruits_copy = fruits.copy()
    assert fruits_copy == ['grape', 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

    # list.reverse()
    # Reverse the elements of the list in place.
    # 原地反转列表中的元素。
    fruits_copy.reverse()
    assert fruits_copy == [
        'banana',
        'apple',
        'kiwi',
        'banana',
        'pear',
        'apple',
        'orange',
        'grape',
    ]

    # list.sort(key=None, reverse=False)
    # Sorts in place (modifies the list directly).
    # 原地排序（直接修改列表）。

    # Alphabetical ascending (default)
    # 字母升序排序（默认）。
    fruits_copy.sort()
    print(fruits_copy)  # ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']

    # Alphabetical descending
    # 字母降序排序。
    fruits_copy.sort(reverse=True)
    print(fruits_copy)  # ['pear', 'orange', 'kiwi', 'grape', 'banana', 'banana', 'apple', 'apple']

    # Sort by string length using key=len
    # 使用 key=len 按字符串长度排序。
    fruits_copy.sort(key=len)
    print(fruits_copy)  # ['pear', 'kiwi', 'apple', 'apple', 'grape', 'banana', 'banana', 'orange']

    fruits_copy.sort()
    assert fruits_copy == [
        'apple',
        'apple',
        'banana',
        'banana',
        'grape',
        'kiwi',
        'orange',
        'pear',
    ]

    # list.pop([i])
    # Remove the item at the given position in the list, and return it. If no index is specified,
    # a.pop() removes and returns the last item in the list. (The square brackets around the i in
    # the method signature denote that the parameter is optional, not that you should type square
    # brackets at that position.)
    # 删除并返回列表中指定位置的元素。若不指定索引，则删除并返回最后一个元素。
    assert fruits == ['grape', 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    assert fruits.pop() == 'banana'
    assert fruits == ['grape', 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple']

    # list.clear()
    # Remove all items from the list. Equivalent to del a[:].
    # 删除列表中的所有元素，等价于 del a[:]。
    fruits.clear()
    assert fruits == []

    # range() — generates a sequence of numbers, often used with lists.
    # range() — 生成数字序列，常与列表搭配使用。

    # range(stop) — starts at 0, stops before stop
    # range(stop) — 从 0 开始，在 stop 之前结束。
    print(list(range(5)))               # [0, 1, 2, 3, 4]
    assert list(range(5)) == [0, 1, 2, 3, 4]

    # range(start, stop) — starts at start, stops before stop
    # range(start, stop) — 从 start 开始，在 stop 之前结束。
    print(list(range(5, 10)))           # [5, 6, 7, 8, 9]
    assert list(range(5, 10)) == [5, 6, 7, 8, 9]

    # range(start, stop, step) — increments by step each time
    # range(start, stop, step) — 每次按 step 递增。
    print(list(range(0, 10, 3)))        # [0, 3, 6, 9]
    assert list(range(0, 10, 3)) == [0, 3, 6, 9]

    # negative step — counts down
    # 负步长 — 倒数计数。
    print(list(range(-10, -100, -30)))  # [-10, -40, -70]
    assert list(range(-10, -100, -30)) == [-10, -40, -70]


def test_del_statement():
    """The del statement

    There is a way to remove an item from a list given its index instead of its value: the del
    statement. This differs from the pop() method which returns a value. The del statement can also
    be used to remove slices from a list or clear the entire list (which we did earlier by
    assignment of an empty list to the slice).
    """

    numbers = [-1, 1, 66.25, 333, 333, 1234.5]

    del numbers[0]
    assert numbers == [1, 66.25, 333, 333, 1234.5]

    del numbers[2:4]
    assert numbers == [1, 66.25, 1234.5]

    del numbers[:]
    assert numbers == []

    # del can also be used to delete entire variables:
    # del 也可以用于删除整个变量。
    del numbers
    with pytest.raises(Exception):
        # Referencing the name a hereafter is an error (at least until another
        # value is assigned to it).
        assert numbers == []


def test_list_comprehensions():
    """List Comprehensions.

    List comprehensions provide a concise way to create lists. Common applications are to make new
    lists where each element is the result of some operations applied to each member of another
    sequence or iterable, or to create a subsequence of those elements that satisfy a certain
    condition.

    A list comprehension consists of brackets containing an expression followed by a for clause,
    then zero or more for or if clauses. The result will be a new list resulting from evaluating
    the expression in the context of the for and if clauses which follow it.
    """

    # For example, assume we want to create a list of squares, like:
    # 例如，假设我们想创建一个平方数列表：
    squares = []
    # range(10) generates numbers from 0 to 9
    # range(10) 生成从 0 到 9 的数字。
    for number in range(10):
        squares.append(number ** 2)

    assert squares == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    # Note that this creates (or overwrites) a variable named "number" that still exists after
    # the loop completes. We can calculate the list of squares without any side effects using:
    # map(lambda x: x**2, range(10)) applies the lambda to each number in range(10)
    # list() converts the map object to a list
    # 注意，这会创建（或覆盖）一个名为"number"的变量，循环结束后该变量仍然存在。
    # 可以使用以下方式无副作用地计算平方数列表：
    # map(lambda x: x**2, range(10)) 将 lambda 应用于 range(10) 中的每个数字，
    # list() 将 map 对象转换为列表。

    """
    Breaking down list(map(lambda x: x ** 2, range(10))):
    ┌──────────────────┬──────────────────────────────────┐
    │       Part       │             Meaning              │
    ├──────────────────┼──────────────────────────────────┤
    │ range(10)        │ numbers 0 to 9                   │
    ├──────────────────┼──────────────────────────────────┤
    │ lambda x: x ** 2 │ function: square each number     │
    ├──────────────────┼──────────────────────────────────┤
    │ map(...)         │ applies the lambda to every item │
    ├──────────────────┼──────────────────────────────────┤
    │ list(...)        │ converts map result to a list    │
    └──────────────────┴──────────────────────────────────┘
    """
    squares = list(map(lambda x: x ** 2, range(10)))
    print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    assert squares == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    # or, equivalently (which is more concise and readable):
    # 或者等价地（更简洁易读）：
    squares = [x ** 2 for x in range(10)]
    assert squares == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    # For example, this listcomp combines the elements of two lists if they are not equal.
    # 例如，以下列表推导式将两个列表中不相等的元素组合在一起。
    combinations = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
    assert combinations == [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

    # and it’s equivalent to:
    # 这等价于：
    combinations = []
    for first_number in [1, 2, 3]:
        for second_number in [3, 1, 4]:
            if first_number != second_number:
                combinations.append((first_number, second_number))

    assert combinations == [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

    # Note how the order of the for and if statements is the same in both these snippets.
    # 注意两段代码中 for 和 if 语句的顺序是相同的。

    # If the expression is a tuple (e.g. the (x, y) in the previous example),
    # it must be parenthesized.
    # 如果表达式是元组（如上例中的 (x, y)），必须加括号。

    # Let's see some more examples:
    # 让我们再看一些示例：

    vector = [-4, -2, 0, 2, 4]

    # Create a new list with the values doubled.
    # 创建一个所有值翻倍的新列表。
    doubled_vector = [x * 2 for x in vector]
    assert doubled_vector == [-8, -4, 0, 4, 8]

    # Filter the list to exclude negative numbers.
    # 过滤列表以排除负数。
    positive_vector = [x for x in vector if x >= 0]
    assert positive_vector == [0, 2, 4]

    # Apply a function to all the elements.
    # 对所有元素应用函数。
    abs_vector = [abs(x) for x in vector]
    assert abs_vector == [4, 2, 0, 2, 4]

    # Call a method on each element.
    # 对每个元素调用方法。
    fresh_fruit = ['  banana', '  loganberry ', 'passion fruit  ']
    clean_fresh_fruit = [weapon.strip() for weapon in fresh_fruit]
    assert clean_fresh_fruit == ['banana', 'loganberry', 'passion fruit']

    # Create a list of 2-tuples like (number, square).
    # 创建形如 (数字, 平方) 的二元组列表。
    square_tuples = [(x, x ** 2) for x in range(6)]
    assert square_tuples == [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

    # Flatten a list using a listcomp with two 'for'.
    # for elem in vector  → iterates over each sublist: [1,2,3], [4,5,6], [7,8,9]
    # for num in elem     → iterates over each number inside the sublist
    # 使用带两个 for 的列表推导式展平列表。
    # for elem in vector  → 遍历每个子列表：[1,2,3], [4,5,6], [7,8,9]
    # for num in elem     → 遍历子列表内的每个数字。
    vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flatten_vector = [num for elem in vector for num in elem]
    print(flatten_vector)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert flatten_vector == [1, 2, 3, 4, 5, 6, 7, 8, 9]

     # Good example: filter even numbers from a nested list
     # 好例子：从嵌套列表中过滤偶数。
    numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    evens = [num for row in numbers for num in row if num % 2 == 0]
    print(evens)  # [2, 4, 6, 8]
    assert evens == [2, 4, 6, 8]

    # Good example: multiplication table (3x3)
    # 好例子：乘法表（3x3）。
    table = [[i * j for j in range(1, 4)] for i in range(1, 4)]
    print(table)  # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
    assert table == [[1, 2, 3], [2, 4, 6], [3, 6, 9]]


def test_nested_list_comprehensions():
    """Nested List Comprehensions

    The initial expression in a list comprehension can be any arbitrary expression, including
    another list comprehension.
    """

    # Consider the following example of a 3x4 matrix implemented as a list of 3 lists of length 4:
    # 考虑以下示例：一个 3x4 矩阵，用包含 3 个长度为 4 的列表的列表来实现。
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]

    # The following list comprehension will transpose rows and columns:
    # 以下列表推导式将对行和列进行转置。
    transposed_matrix = [[row[i] for row in matrix] for i in range(4)]
    assert transposed_matrix == [
        [1, 5, 9],
        [2, 6, 10],
        [3, 7, 11],
        [4, 8, 12],
    ]

    # As we saw in the previous section, the nested listcomp is evaluated in the context of the
    # for that follows it, so this example is equivalent to:
    # 如上一节所见，嵌套列表推导式在其后的 for 语句的上下文中求值，因此本例等价于：
    transposed = []
    for i in range(4):
        transposed.append([row[i] for row in matrix])

    assert transposed == [
        [1, 5, 9],
        [2, 6, 10],
        [3, 7, 11],
        [4, 8, 12],
    ]

    # which, in turn, is the same as:
    # 这又等价于：
    transposed = []
    for i in range(4):
        # the following 3 lines implement the nested listcomp
        # 以下 3 行实现了嵌套列表推导式的逻辑。
        transposed_row = []
        for row in matrix:
            transposed_row.append(row[i])
        transposed.append(transposed_row)

    assert transposed == [
        [1, 5, 9],
        [2, 6, 10],
        [3, 7, 11],
        [4, 8, 12],
    ]

    # In the real world, you should prefer built-in functions to complex flow statements.
    # The zip() function would do a great job for this use case:
    # 在实际开发中，应优先使用内置函数而非复杂的流程控制语句。
    # zip() 函数非常适合这种场景。
    assert list(zip(*matrix)) == [
        (1, 5, 9),
        (2, 6, 10),
        (3, 7, 11),
        (4, 8, 12),
    ]

