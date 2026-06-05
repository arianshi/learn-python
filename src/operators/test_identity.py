"""Identity operators

身份运算符 (Identity Operators)

@see: https://www.w3schools.com/python/python_operators.asp

Identity operators are used to compare the objects, not if they are equal,
but if they are actuallythe same object, with the same memory location.

身份运算符用于比较对象，并不是判断它们是否相等，
而是判断它们是否实际上是同一个对象（即拥有相同的内存地址）。
"""


def test_identity_operators():
    """Identity operators"""
    # 身份运算符

    # Let's illustrate identity operators based on the following lists.
    # 让我们基于以下列表来演示身份运算符。
    first_fruits_list = ["apple", "banana"]
    second_fruits_list = ["apple", "banana"]
    third_fruits_list = first_fruits_list

    # is
    # Returns true if both variables are the same object.
    # is 运算符
    # 如果两个变量是同一个对象，则返回 True。

    # Example:
    # first_fruits_list and third_fruits_list are the same objects.
    # 示例：
    # first_fruits_list 和 third_fruits_list 是同一个对象。
    print(first_fruits_list is third_fruits_list)       # True
    assert first_fruits_list is third_fruits_list

    print(first_fruits_list is second_fruits_list)      # False

    # is not
    # Returns true if both variables are not the same object.
    # is not 运算符
    # 如果两个变量不是同一个对象，则返回 True。

    # Example:
    # first_fruits_list and second_fruits_list are not the same objects, even if they have
    # the same content
    # 示例：
    # first_fruits_list 和 second_fruits_list 不是同一个对象，
    # 即使它们的内容相同。
    print(first_fruits_list is not second_fruits_list)  # True
    assert first_fruits_list is not second_fruits_list

    # "is" checks same memory location (identity); "==" checks same value (equality).
    # second_fruits_list has the same content but is a different object in memory.
    # "is" 检查是否在同一内存地址（身份相同）；"==" 检查是否值相等（内容相同）。
    # second_fruits_list 内容相同，但在内存中是不同的对象。
    print(first_fruits_list is second_fruits_list)      # False  (different objects)
    print(first_fruits_list == second_fruits_list)      # True   (same content)
    assert first_fruits_list is not second_fruits_list
    assert first_fruits_list == second_fruits_list
