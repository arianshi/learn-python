"""File Wildcards.

文件通配符 (File Wildcards)

@see: https://docs.python.org/3/tutorial/stdlib.html#file-wildcards

The glob module provides a function for making file lists from directory wildcard searches:

glob 模块提供了一个函数，可以通过目录通配符搜索来生成文件列表：
"""

import glob


def test_glob():
    """File Wildcards."""
    # 文件通配符

    # == operator for lists relies on the order of elements in the list.
    # In some cases (like on Linux Mint, python3.6) the glob() function returns list
    # in reverse order then  it might be expected. Thus lets sort both lists before comparison
    # using sorted() built-in function.
    # 列表的 == 运算符依赖于列表中元素的顺序。
    # 在某些情况下（例如在 Linux Mint, python3.6 上）, glob() 函数返回的列表顺序
    # 可能与预期相反。因此，在比较之前我们使用内置函数 sorted() 对两个列表进行排序。
    assert sorted(glob.glob('src/standard_libraries/glob_files/*.txt')) == sorted([
        'src/standard_libraries/glob_files/first_file.txt',
        'src/standard_libraries/glob_files/second_file.txt'
    ])
