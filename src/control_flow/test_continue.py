"""CONTINUE statement

CONTINUE 语句 (CONTINUE statement)

@see: https://docs.python.org/3/tutorial/controlflow.html

The continue statement is borrowed from C, continues with the next iteration of the loop.

continue 语句借鉴自 C 语言，作用是继续执行循环的下一次迭代。
"""


def test_continue_statement():
    """CONTINUE statement in FOR loop"""
    # FOR 循环中的 CONTINUE 语句

    # Let's
    # 让我们开始吧

    # This list will contain only even numbers from the range.
    # 这个列表将只包含范围内的偶数。
    even_numbers = []
    # This list will contain every other numbers (in this case - ods).
    # 这个列表将包含其余的数字（在本例中是奇数）。
    rest_of_the_numbers = []

    for number in range(0, 10):
        # Check if remainder after division is zero (which would mean that number is even).
        # 检查除法后的余数是否为零（如果为零则表示该数字是偶数）。
        if number % 2 == 0:
            even_numbers.append(number)
            # Stop current loop iteration and go to the next one immediately.
            # 停止当前的循环迭代，立即进入下一次迭代。
            continue

        rest_of_the_numbers.append(number)

    assert even_numbers == [0, 2, 4, 6, 8]
    assert rest_of_the_numbers == [1, 3, 5, 7, 9]
