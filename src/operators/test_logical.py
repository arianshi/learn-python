"""Logical operators

逻辑运算符 (Logical Operators)

@see: https://www.w3schools.com/python/python_operators.asp

Logical operators are used to combine conditional statements.

逻辑运算符用于组合条件语句。
"""


def test_logical_operators():
    """Logical operators"""
    # 逻辑运算符

    # Let's work with these number to illustrate logic operators.
    # 让我们使用以下数字来演示逻辑运算符。
    first_number = 5
    second_number = 10

    # and
    # Returns True if both statements are true.
    # and 运算符
    # 当两个语句都为真时返回 True。
    assert first_number > 0 and second_number < 20

    # or
    # Returns True if one of the statements is true
    # or 运算符
    # 当两个语句中至少有一个为真时返回 True。
    assert first_number > 5 or second_number < 20

    # not
    # Reverse the result, returns False if the result is true.
    # not 运算符
    # 对结果取反，如果原本为 True 则返回 False。
    # pylint: disable=unneeded-not
    assert not first_number == second_number
    assert first_number != second_number
