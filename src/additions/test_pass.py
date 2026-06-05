"""PASS statement

PASS 语句

@see: https://docs.python.org/3/tutorial/controlflow.html

The pass statement does nothing. It can be used when a statement is required syntactically but
the program requires no action.

pass 语句什么也不做。它可以在语法上需要一条语句但程序逻辑上不需要任何操作时使用。
"""


def test_pass_in_function():
    """PASS statement in function

    "Pass" can be used as a place-holder for a function or conditional body when you are working on
    new code, allowing you to keep thinking at a more abstract level.

    The pass statement below is silently ignored but it makes current test_pass() function valid.
    """
    # 函数中的 PASS 语句
    # 当你在编写新代码时，"pass" 可以用作函数或条件语句体的占位符，
    # 让你能够继续在更抽象的层面思考问题。
    # 下面的 pass 语句会被静默忽略，但它使得当前的 test_pass() 函数在语法上有效。
    pass


def test_pass_in_loop():
    """PASS in loops.

    "Pass" can be used when a statement is required syntactically but the program requires no
    action. For example:
    """
    # 循环中的 PASS。
    # 当语法上需要一条语句但程序逻辑上不需要任何操作时，可以使用 "pass"。例如：

    # pylint: disable=unused-variable
    for number in range(100):
        # It just don't do anything but for loop is still valid.
        # 它什么都不做，但 for 循环仍然是有效的。
        pass

    # Example above is quite useless but it was given just for illustration of the idea.
    # The more useful example might be:
    #
    # while True:
    #   pass  # Busy-wait for keyboard interrupt (Ctrl+C)
    # 上面的例子用处不大，给出它只是为了说明这个概念。
    # 一个更有用的例子可能是：
    #
    # while True:
    #   pass  # 忙等待键盘中断 (Ctrl+C)


# pylint: disable=too-few-public-methods
class MyEmptyClass:
    """PASS statement in class

    "Pass" is commonly used for creating minimal classes like current one.
    """
    # 类中的 PASS 语句
    # "Pass" 常用于创建像当前这样的最小类。
    pass
