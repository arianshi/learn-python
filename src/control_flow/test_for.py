"""FOR statement

FOR 语句 (FOR statement)

@see: https://docs.python.org/3/tutorial/controlflow.html

The for statement in Python differs a bit from what you may be used to in C or Pascal.
Rather than always iterating over an arithmetic progression of numbers (like in Pascal), or
giving the user the ability to define both the iteration step and halting condition (as C),
Python’s for statement iterates over the items of any sequence (a list or a string), in the
order that they appear in the sequence. For example (no pun intended):

Python 中的 for 语句与你在 C 或 Pascal 中习惯的写法略有不同。
它不是总是对一个算术级数进行迭代（如 Pascal 那样），也不是让用户同时定义迭代步长和
终止条件（如 C 那样）；Python 的 for 语句会按照元素在序列（如列表或字符串）中出现
的顺序，对任意序列中的元素进行迭代。例如：
"""


# pylint: disable=too-many-locals
def test_for_statement():
    """FOR statement"""
    # FOR 语句

    # Measure some strings:
    # 测量一些字符串的长度：
    words = ['cat', 'window', 'defenestrate']
    words_length = 0

    for word in words:
        words_length += len(word)

    # "cat" length is 3
    # "window" length is 6
    # "defenestrate" length is 12
    # "cat" 长度是 3
    # "window" 长度是 6
    # "defenestrate" 长度是 12
    assert words_length == (3 + 6 + 12)

    # If you need to modify the sequence you are iterating over while inside the loop
    # (for example to duplicate selected items), it is recommended that you first make a copy.
    # Iterating over a sequence does not implicitly make a copy. The slice notation makes this
    # especially convenient:
    # 如果你需要在循环中修改正在迭代的序列（例如复制某些选定的项），建议先创建一份副本。
    # 对序列进行迭代并不会隐式地创建副本。切片语法使这一操作特别方便：
    for word in words[:]:  # Loop over a slice copy of the entire list.
        if len(word) > 6:
            words.insert(0, word)

    # Otherwise with for w in words:, the example would attempt to create an infinite list,
    # inserting defenestrate over and over again.
    # 否则，如果直接使用 for w in words:，该示例将会试图创建一个无限列表，
    # 一遍又一遍地插入 defenestrate。

    assert words == ['defenestrate', 'cat', 'window', 'defenestrate']

    # If you do need to iterate over a sequence of numbers, the built-in function range() comes in
    # handy. It generates arithmetic progressions:
    # 如果你确实需要遍历一个数字序列，内置函数 range() 就会派上用场。它会生成等差数列：
    iterated_numbers = []

    for number in range(5):
        iterated_numbers.append(number)
        print(number)  # 0, 1, 2, 3, 4

    assert iterated_numbers == [0, 1, 2, 3, 4]

    # To iterate over the indices of a sequence, you can combine range() and len() as follows:
    # 要遍历序列的索引，可以像下面这样将 range() 和 len() 结合使用：
    words = ['Mary', 'had', 'a', 'little', 'lamb']
    concatenated_string = ''

    # pylint: disable=consider-using-enumerate
    for word_index in range(len(words)):
        concatenated_string += words[word_index] + ' '

    assert concatenated_string == 'Mary had a little lamb '

    # Or simply use enumerate().
    # 或者直接使用 enumerate()。
    concatenated_string = ''

    for word_index, word in enumerate(words):
        concatenated_string += word + ' '

    assert concatenated_string == 'Mary had a little lamb '

    # When looping through dictionaries, the key and corresponding value can be retrieved at the
    # same time using the items() method.
    # 在遍历字典时，可以使用 items() 方法同时获取键和对应的值。
    knights_names = []
    knights_properties = []

    knights = {'gallahad': 'the pure', 'robin': 'the brave'}
    for key, value in knights.items():
        knights_names.append(key)
        knights_properties.append(value)

    assert knights_names == ['gallahad', 'robin']
    assert knights_properties == ['the pure', 'the brave']

    # When looping through a sequence, the position index and corresponding value can be retrieved
    # at the same time using the enumerate() function
    # 在遍历一个序列时，可以使用 enumerate() 函数同时获取位置索引和对应的值。
    indices = []
    values = []
    for index, value in enumerate(['tic', 'tac', 'toe']):
        indices.append(index)
        values.append(value)

    assert indices == [0, 1, 2]
    assert values == ['tic', 'tac', 'toe']

    # To loop over two or more sequences at the same time, the entries can be paired with
    # the zip() function.
    # 要同时遍历两个或更多的序列，可以使用 zip() 函数将各项配对。
    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    combinations = []

    for question, answer in zip(questions, answers):
        combinations.append('What is your {0}?  It is {1}.'.format(question, answer))

    assert combinations == [
        'What is your name?  It is lancelot.',
        'What is your quest?  It is the holy grail.',
        'What is your favorite color?  It is blue.',
    ]


def test_range_function():
    """Range function

    Range 函数 (Range function)

    If you do need to iterate over a sequence of numbers, the built-in function range() comes in
    handy. It generates arithmetic progressions.

    如果你确实需要遍历一个数字序列，内置函数 range() 就会派上用场。它会生成等差数列。

    In many ways the object returned by range() behaves as if it is a list, but in fact it isn’t.
    It is an object which returns the successive items of the desired sequence when you iterate
    over it, but it doesn’t really make the list, thus saving space.

    在许多方面，range() 返回的对象表现得就像一个列表，但实际上并不是。
    它是一个对象，当你对其进行迭代时会依次返回所需序列中的元素，但它并不真正创建列表，
    因此可以节省内存空间。

    We say such an object is iterable, that is, suitable as a target for functions and constructs
    that expect something from which they can obtain successive items until the supply is exhausted.
    We have seen that the for statement is such an iterator. The function list() is another; it
    creates lists from iterables:

    我们把这样的对象称为可迭代对象（iterable），意思是说它适合作为那些期望从中依次获取
    元素直到耗尽的函数和结构的目标。我们已经看到 for 语句就是这样的一个迭代器；
    list() 函数是另一个，它会从可迭代对象中创建列表：
    """

    # range(stop) — starts at 0, stops before stop
    # range(stop) —— 从 0 开始，在 stop 之前结束
    print(list(range(5)))             # [0, 1, 2, 3, 4]
    assert list(range(5)) == [0, 1, 2, 3, 4]

    # range(start, stop) — starts at start, stops before stop
    # range(start, stop) —— 从 start 开始，在 stop 之前结束
    print(list(range(5, 10)))         # [5, 6, 7, 8, 9]
    assert list(range(5, 10)) == [5, 6, 7, 8, 9]

    # range(start, stop, step) — increments by step each time
    # range(start, stop, step) —— 每次按 step 递增
    print(list(range(0, 10, 3)))      # [0, 3, 6, 9]
    assert list(range(0, 10, 3)) == [0, 3, 6, 9]

    # negative step — counts down
    # 负的步长 —— 倒序计数
    print(list(range(-10, -100, -30)))  # [-10, -40, -70]
    assert list(range(-10, -100, -30)) == [-10, -40, -70]
