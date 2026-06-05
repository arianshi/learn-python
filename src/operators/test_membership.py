"""Membership operators

成员运算符 (Membership Operators)

@see: https://www.w3schools.com/python/python_operators.asp

Membership operators are used to test if a sequence is presented in an object.

成员运算符用于测试某个序列是否存在于一个对象中。
"""


def test_membership_operators():
    """Membership operators"""
    # 成员运算符

    # Let's use the following fruit list to illustrate membership concept.
    # 让我们使用以下水果列表来演示成员关系的概念。
    fruit_list = ["apple", "banana"]

    # in
    # Returns True if a sequence with the specified value is present in the object.
    # in 运算符
    # 如果指定值的序列存在于该对象中，则返回 True。

    # Returns True because a sequence with the value "banana" is in the list
    # 返回 True，因为列表中存在值为 "banana" 的元素。
    assert "banana" in fruit_list

    # not in
    # Returns True if a sequence with the specified value is not present in the object
    # not in 运算符
    # 如果指定值的序列不存在于该对象中，则返回 True。

    # Returns True because a sequence with the value "pineapple" is not in the list.
    # 返回 True，因为列表中不存在值为 "pineapple" 的元素。
    assert "pineapple" not in fruit_list
