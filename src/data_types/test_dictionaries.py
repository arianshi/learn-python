"""Dictionaries.

字典 (Dictionaries)

@see: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
@see: https://www.w3schools.com/python/python_dictionaries.asp

A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are
written with curly brackets, and they have keys and values.

字典是一种无序、可变且带索引的集合。在 Python 中，字典使用花括号书写，包含键和值。

Dictionaries are sometimes found in other languages as “associative memories” or “associative
arrays”. Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by
keys, which can be any immutable type; strings and numbers can always be keys. Tuples can be used
as keys if they contain only strings, numbers, or tuples; if a tuple contains any mutable object
either directly or indirectly, it cannot be used as a key. You can’t use lists as keys, since
lists can be modified in place using index assignments, slice assignments, or methods like append()
and extend().

字典在其他语言中有时被称为「关联内存」或「关联数组」。与通过数字范围索引的序列不同，
字典通过键来索引，键可以是任何不可变类型；字符串和数字总是可以作为键。
如果元组只包含字符串、数字或元组，也可以用作键；如果元组直接或间接包含任何可变对象，
则不能用作键。列表不能用作键，因为列表可以通过索引赋值、切片赋值，或像 append() 和 extend()
之类的方法被原地修改。

It is best to think of a dictionary as a set of key: value pairs, with the requirement that the
keys are unique (within one dictionary). A pair of braces creates an empty dictionary: {}.
Placing a comma-separated list of key:value pairs within the braces adds initial key:value pairs
to the dictionary; this is also the way dictionaries are written on output.

最好将字典视为一组 键: 值 对的集合，要求键在同一个字典中是唯一的。一对花括号创建一个空字典：{}。
在花括号内放入用逗号分隔的键:值对列表，可以为字典添加初始的键值对；这也是字典输出时的书写形式。
"""


def test_dictionary():
    """Dictionary"""
    # 字典

    fruits_dictionary = {
        'cherry': 'red',
        'apple': 'green',
        'banana': 'yellow',
    }

    assert isinstance(fruits_dictionary, dict)

    # You may access set elements by keys.
    # 可以通过键来访问字典元素。
    assert fruits_dictionary['apple'] == 'green'
    assert fruits_dictionary['banana'] == 'yellow'
    assert fruits_dictionary['cherry'] == 'red'

    # To check whether a single key is in the dictionary, use the in keyword.
    # 使用 in 关键字检查某个键是否在字典中。
    assert 'apple' in fruits_dictionary
    assert 'pineapple' not in fruits_dictionary

    # Change the apple color to "red".
    # 将苹果的颜色改为"red"。
    fruits_dictionary['apple'] = 'red'

    # Add new key/value pair to the dictionary
    # 向字典中添加新的键值对。
    fruits_dictionary['pineapple'] = 'yellow'
    assert fruits_dictionary['pineapple'] == 'yellow'

    # Performing list(d) on a dictionary returns a list of all the keys used in the dictionary,
    # in insertion order (if you want it sorted, just use sorted(d) instead).
    # 对字典执行 list(d) 会按插入顺序返回所有键的列表（若需排序，可使用 sorted(d)）。
    assert list(fruits_dictionary) == ['cherry', 'apple', 'banana', 'pineapple']
    assert sorted(fruits_dictionary) == ['apple', 'banana', 'cherry', 'pineapple']

    # It is also possible to delete a key:value pair with del.
    # 也可以使用 del 删除一个键值对。
    del fruits_dictionary['pineapple']
    assert list(fruits_dictionary) == ['cherry', 'apple', 'banana']

    # The dict() constructor builds dictionaries directly from sequences of key-value pairs.
    # dict() 构造函数可以直接从键值对序列中构建字典。
    dictionary_via_constructor = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

    assert dictionary_via_constructor['sape'] == 4139
    assert dictionary_via_constructor['guido'] == 4127
    assert dictionary_via_constructor['jack'] == 4098

    # In addition, dict comprehensions can be used to create dictionaries from arbitrary key
    # and value expressions:
    # 此外，字典推导式可以通过任意键和值表达式来创建字典。
    dictionary_via_expression = {x: x**2 for x in (2, 4, 6)}
    assert dictionary_via_expression[2] == 4
    assert dictionary_via_expression[4] == 16
    assert dictionary_via_expression[6] == 36

    # When the keys are simple strings, it is sometimes easier to specify pairs using
    # keyword arguments.
    # 当键是简单字符串时，有时使用关键字参数指定键值对更为方便。
    dictionary_for_string_keys = dict(sape=4139, guido=4127, jack=4098)
    assert dictionary_for_string_keys['sape'] == 4139
    assert dictionary_for_string_keys['guido'] == 4127
    assert dictionary_for_string_keys['jack'] == 4098
