"""Bitwise operators

位运算符 (Bitwise Operators)

@see: https://www.w3schools.com/python/python_operators.asp

Bitwise operators manipulate numbers on bit level.

位运算符在比特（bit）层面上对数字进行操作。
"""


def test_bitwise_operators():
    """Bitwise operators"""
    # 位运算符

    # AND
    # Sets each bit to 1 if both bits are 1.
    #
    # Example:
    # 5 = 0b0101
    # 3 = 0b0011
    # 按位与（AND）
    # 仅当两个对应位都为 1 时，结果位才为 1。
    #
    # 示例：
    # 5 = 0b0101
    # 3 = 0b0011
    assert 5 & 3 == 1  # 0b0001

    # OR
    # Sets each bit to 1 if one of two bits is 1.
    #
    # Example:
    # 5 = 0b0101
    # 3 = 0b0011
    # 按位或（OR）
    # 只要两个对应位中有一个为 1，结果位就为 1。
    #
    # 示例：
    # 5 = 0b0101
    # 3 = 0b0011
    assert 5 | 3 == 7  # 0b0111

    # NOT
    # Inverts all the bits.
    # 按位取反（NOT）
    # 将所有的位翻转（0 变 1，1 变 0）。
    assert ~5 == -6

    # XOR
    # Sets each bit to 1 if only one of two bits is 1.
    #
    # Example:
    # 5 = 0b0101
    # 3 = 0b0011
    # 按位异或（XOR）
    # 仅当两个对应位中恰好有一个为 1 时，结果位才为 1。
    #
    # 示例：
    # 5 = 0b0101
    # 3 = 0b0011
    number = 5  # 0b0101
    number ^= 3  # 0b0011
    assert 5 ^ 3 == 6  # 0b0110

    # Signed right shift
    # Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost
    # bits fall off.
    #
    # Example:
    # 5 = 0b0101
    # 带符号右移
    # 向右移位时，从左侧填入最左位（符号位）的副本，最右侧的位被丢弃。
    #
    # 示例：
    # 5 = 0b0101
    assert 5 >> 1 == 2  # 0b0010
    assert 5 >> 2 == 1  # 0b0001

    # Zero fill left shift
    # Shift left by pushing zeros in from the right and let the leftmost bits fall off.
    #
    # Example:
    # 5 = 0b0101
    # 零填充左移
    # 向左移位时，从右侧填入 0，最左侧的位被丢弃。
    #
    # 示例：
    # 5 = 0b0101
    assert 5 << 1 == 10  # 0b1010
    assert 5 << 2 == 20  # 0b10100
