"""Comparison operators

比较运算符 (Comparison Operators)

@see: https://www.w3schools.com/python/python_operators.asp

Comparison operators are used to compare two values.

比较运算符用于比较两个值。
"""


def test_comparison_operators():
    """Comparison operators"""
    # 比较运算符

    # Equal.
    # 等于。
    number = 5
    assert number == 5

    # Not equal.
    # 不等于。
    number = 5
    assert number != 3

    # Greater than.
    # 大于。
    number = 5
    assert number > 3

    # Less than.
    # 小于。
    number = 5
    assert number < 8

    # Greater than or equal to
    # 大于或等于。
    number = 5
    assert number >= 5
    assert number >= 4

    # Less than or equal to
    # 小于或等于。
    number = 5
    assert number <= 5
    assert number <= 6
