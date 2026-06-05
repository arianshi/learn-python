"""BREAK statement

BREAK 语句 (BREAK statement)

@see: https://docs.python.org/3/tutorial/controlflow.html

The break statement, like in C, breaks out of the innermost enclosing "for" or "while" loop.

与 C 语言中类似，break 语句会跳出最内层的 "for" 或 "while" 循环。
"""


def test_break_statement():
    """BREAK statement"""
    # BREAK 语句

    # Let's terminate the loop in case if we've found the number we need in a range from 0 to 100.
    # 如果我们在 0 到 100 的范围内找到了所需的数字，就终止循环。
    number_to_be_found = 42
    # This variable will record how many time we've entered the "for" loop.
    # 这个变量将记录我们进入 "for" 循环的次数。
    number_of_iterations = 0

    for number in range(100):
        if number == number_to_be_found:
            # Break here and don't continue the loop.
            # 在这里跳出循环，不再继续。
            break
        else:
            number_of_iterations += 1

    # We need to make sure that break statement has terminated the loop once it found the number.
    # 我们需要确保 break 语句在找到该数字后立即终止了循环。
    assert number_of_iterations == 42
