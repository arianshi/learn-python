"""Numbers.

@see: https://docs.python.org/3/tutorial/introduction.html
@see: https://www.w3schools.com/python/python_numbers.asp

There are three numeric types in Python:
- int (e.g. 2, 4, 20)
  - bool (e.g. False and True, acting like 0 and 1)
- float (e.g. 5.0, 1.6)
- complex (e.g. 5+6j, 4-3j)
"""


def test_integer_numbers():
    """Integer type

    Int, or integer, is a whole number, positive or negative,
    without decimals, of unlimited length.
    """

    positive_integer = 1
    negative_integer = -3255522
    big_integer = 35656222554887711

    assert isinstance(positive_integer, int)
    assert isinstance(negative_integer, int)
    assert isinstance(big_integer, int)


def test_booleans():
    """Boolean

    Booleans represent the truth values False and True. The two objects representing the values
    False and True are the only Boolean objects. The Boolean type is a subtype of the integer type,
    and Boolean values behave like the values 0 and 1, respectively, in almost all contexts, the
    exception being that when converted to a string, the strings "False" or "True" are returned,
    respectively.
    """

    true_boolean = True
    false_boolean = False

    assert true_boolean
    assert not false_boolean

    assert isinstance(true_boolean, bool)
    assert isinstance(false_boolean, bool)

    # Let's try to cast boolean to string.
    # 尝试将布尔值转换为字符串。
    assert str(true_boolean) == "True"
    assert str(false_boolean) == "False"


def test_float_numbers():
    """Float type

    Float, or "floating point number" is a number, positive or negative,
    containing one or more decimals.
    """

    float_number = 7.0
    # Another way of declaring float is using float() function.
    # 另一种声明浮点数的方式是使用 float() 函数。
    float_number_via_function = float(7)
    float_negative = -35.59

    assert float_number == float_number_via_function
    assert isinstance(float_number, float)
    assert isinstance(float_number_via_function, float)
    assert isinstance(float_negative, float)

    # Float can also be scientific numbers with an "e" to indicate
    # the power of 10.
    # 浮点数也可以用科学计数法表示，用"e"表示 10 的幂次。
    float_with_small_e = 35e3
    float_with_big_e = 12E4

    assert float_with_small_e == 35000
    assert float_with_big_e == 120000
    assert isinstance(12E4, float)
    assert isinstance(-87.7e100, float)


def test_complex_numbers():
    """Complex Type"""

    complex_number_1 = 5 + 6j
    complex_number_2 = 3 - 2j

    assert isinstance(complex_number_1, complex)
    assert isinstance(complex_number_2, complex)
    assert complex_number_1 * complex_number_2 == 27 + 8j


def test_number_operators():
    """Basic operations"""

    # Addition.
    # 加法。
    assert 2 + 4 == 6

    # Multiplication.
    # 乘法。
    assert 2 * 4 == 8

    # Division always returns a floating point number.
    # 除法始终返回浮点数。
    assert 12 / 3 == 4.0
    assert 12 / 5 == 2.4
    assert 17 / 3 == 5.666666666666667

    # Modulo operator returns the remainder of the division.
    # 取模运算符返回除法的余数。
    assert 12 % 3 == 0
    assert 13 % 3 == 1

    # NEW: Floor division discards the fractional part. 17 // 3 = 5 (remainder 2)
    # 整除：丢弃小数部分。17 // 3 = 5（余 2）。
    assert 17 // 3 == 5

    # Raising the number to specific power.
    # 对数字进行幂运算。
    assert 5 ** 2 == 25  # 5 squared
    assert 2 ** 7 == 128  # 2 to the power of 7

    # There is full support for floating point; operators with
    # mixed type operands convert the integer operand to floating point.
    # 完全支持浮点运算；当操作数类型混合时，整数操作数会被转换为浮点数。
    assert 4 * 3.75 - 1 == 14.0
