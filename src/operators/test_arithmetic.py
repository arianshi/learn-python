"""Arithmetic operators

算术运算符 (Arithmetic Operators)

@see: https://www.w3schools.com/python/python_operators.asp

Arithmetic operators are used with numeric values to perform common mathematical operations

算术运算符用于对数值执行常见的数学运算。
"""


def test_arithmetic_operators():
    """Arithmetic operators"""
    # 算术运算符

    # Addition.
    # 加法。
    assert 5 + 3 == 8

    # Subtraction.
    # 减法。
    assert 5 - 3 == 2

    # Multiplication.
    # 乘法。
    assert 5 * 3 == 15
    assert isinstance(5 * 3, int)

    # Division.
    # Result of division is float number.
    # 除法。
    # 除法的结果是浮点数。
    assert 5 / 3 == 1.6666666666666667
    assert 8 / 4 == 2
    assert isinstance(5 / 3, float)
    assert isinstance(8 / 4, float)

    # Modulus.
    # 取模（求余数）。
    assert 5 % 3 == 2

    # Exponentiation.
    # 幂运算（指数运算）。
    assert 5 ** 3 == 125
    assert 2 ** 3 == 8
    assert 2 ** 4 == 16
    assert 2 ** 5 == 32
    assert isinstance(5 ** 3, int)

    # NOTE Floor division.
    # 注意：地板除（向下取整除法）。
    assert 5 // 3 == 1
    assert 6 // 3 == 2
    assert 7 // 3 == 2
    assert 9 // 3 == 3
    assert isinstance(5 // 3, int)
