"""
Double Asterisk (**)

@see: https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments

The double asterisk (**) operator has several usages in Python:

1. Exponentiation (power calculation)
2. Collect keyword arguments (**kwargs)
3. Unpack dictionaries into function calls
4. Merge dictionaries

双星号（**）在 Python 中主要有以下用途：

1. 幂运算
2. 收集关键字参数（**kwargs）
3. 解包字典作为函数参数
4. 合并字典
"""


def test_exponentiation_operator():
    """Exponentiation operator (幂运算)"""

    # Calculate powers.
    # 计算幂。
    assert 2 ** 3 == 8
    assert 5 ** 2 == 25

    # Calculate square roots.
    # 计算平方根。
    assert 16 ** 0.5 == 4.0
    assert 81 ** 0.5 == 9.0


def test_kwargs_collection():
    """Collect keyword arguments (**kwargs)"""

    def create_user(**kwargs):
        return kwargs

    user = create_user(
        name="Arian",
        age=30,
        country="Singapore",
    )

    # kwargs are collected into a dictionary.
    # kwargs 会被收集成一个字典。
    assert isinstance(user, dict)

    assert user == {
        "name": "Arian",
        "age": 30,
        "country": "Singapore",
    }


def test_dictionary_unpacking():
    """Dictionary unpacking in function calls"""

    def create_user(name, age):
        return {
            "name": name,
            "age": age,
        }

    user_data = {
        "name": "Arian",
        "age": 30,
    }

    # Unpack dictionary into keyword arguments.
    # 将字典解包为关键字参数。
    user = create_user(**user_data)

    assert user == {
        "name": "Arian",
        "age": 30,
    }


def test_dictionary_merge():
    """Dictionary merging"""

    profile = {
        "name": "Arian",
        "age": 30,
    }

    settings = {
        "theme": "dark",
        "language": "en",
    }

    merged = {
        **profile,
        **settings,
    }

    assert merged == {
        "name": "Arian",
        "age": 30,
        "theme": "dark",
        "language": "en",
    }


def test_dictionary_merge_override():
    """Later values override earlier values"""

    first = {
        "name": "Arian",
        "age": 25,
    }

    second = {
        "age": 30,
    }

    merged = {
        **first,
        **second,
    }

    # Values from later dictionaries win.
    # 后面的字典会覆盖前面的值。
    assert merged == {
        "name": "Arian",
        "age": 30,
    }


def test_args_and_kwargs():
    """Difference between *args and **kwargs"""

    def collect(*args, **kwargs):
        return args, kwargs

    args, kwargs = collect(
        1,
        2,
        3,
        name="Arian",
        age=30,
    )

    # *args becomes tuple.
    # *args 会变成 tuple。
    assert args == (1, 2, 3)

    # **kwargs becomes dict.
    # **kwargs 会变成 dict。
    assert kwargs == {
        "name": "Arian",
        "age": 30,
    }