"""WHILE statement

WHILE 语句 (WHILE statement)

@see: https://docs.python.org/3/tutorial/controlflow.html
@see: https://docs.python.org/3/reference/compound_stmts.html#the-while-statement

The while loop executes as long as the condition remains true. In Python, like in C, any
non-zero integer value is true; zero is false. The condition may also be a string or list
value, in fact any sequence; anything with a non-zero length is true, empty sequences are
false.

只要条件保持为真，while 循环就会一直执行。在 Python 中，与 C 类似，任何非零的整数
值都为真，零则为假。条件也可以是字符串或列表值，实际上可以是任何序列；任何长度不为
零的对象都为真，而空序列则为假。

The test used in the example is a simple comparison. The standard comparison operators are
written the same as in C: < (less than), > (greater than), == (equal to), <= (less than or
equal to), >= (greater than or equal to) and != (not equal to).

示例中使用的判断是一个简单的比较。标准的比较运算符的写法与 C 中相同：
< (小于)、> (大于)、== (等于)、<= (小于或等于)、>= (大于或等于) 以及 != (不等于)。
"""


def test_while_statement():
    """WHILE statement"""
    # WHILE 语句

    # Let's raise the number to certain power using while loop.
    # 让我们用 while 循环来计算一个数的若干次方。
    number = 2
    power = 5

    result = 1

    while power > 0:
        result *= number
        power -= 1

    # 2^5 = 32
    assert result == 32
