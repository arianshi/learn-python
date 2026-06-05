"""Errors and Exceptions.

错误与异常 (Errors and Exceptions)

@see: https://docs.python.org/3/tutorial/errors.html#errors-and-exceptions

Even if a statement or expression is syntactically correct, it may cause an error when an attempt
is made to execute it. Errors detected during execution are called exceptions and are not
unconditionally fatal.

即使一个语句或表达式在语法上是正确的，当尝试执行它时仍然可能引发错误。
在执行过程中检测到的错误被称为「异常」(exceptions)，并且它们不一定都是致命的。

It is possible to write programs that handle selected exceptions.

可以编写程序来处理指定的异常。
"""


def test_handle_exceptions():
    """Handling of exceptions

    The try statement works as follows.

    - First, the try clause (the statement(s) between the try and except keywords) is executed.

    - If no exception occurs, the except clause is skipped and execution of the try statement
    is finished.

    - If an exception occurs during execution of the try clause, the rest of the clause is skipped.
    Then if its type matches the exception named after the except keyword, the except clause is
    executed, and then execution continues after the try statement.

    - If an exception occurs which does not match the exception named in the except clause, it is
    passed on to outer try statements; if no handler is found, it is an unhandled exception and
    execution stops with a message.
    """
    # 异常处理
    #
    # try 语句的工作方式如下：
    #
    # - 首先，执行 try 子句（位于 try 和 except 关键字之间的语句）。
    #
    # - 如果没有异常发生，则跳过 except 子句，try 语句执行结束。
    #
    # - 如果在 try 子句执行过程中发生了异常，则子句的剩余部分会被跳过。
    #   接着，如果异常的类型与 except 关键字后指定的异常匹配，则执行 except 子句，
    #   然后在 try 语句之后继续执行。
    #
    # - 如果发生的异常与 except 子句中指定的异常不匹配，则它会被传递给外层的 try 语句；
    #   如果找不到处理程序，则它是一个未处理的异常，执行将停止并显示错误消息。

    # Let's simulate division by zero exception.
    # 让我们模拟一个除以零的异常。
    exception_has_been_handled = False
    try:
        result = 10 * (1 / 0)  # division by zero
        # We should not get here at all.
        # 我们根本不应该执行到这里。
        assert result
    except ZeroDivisionError:
        # We should get here because of division by zero.
        # 因为发生了除以零的错误，所以应该执行到这里。
        exception_has_been_handled = True

    assert exception_has_been_handled

    # Let's simulate undefined variable access exception.
    # 让我们模拟一个访问未定义变量的异常。
    exception_has_been_handled = False
    try:
        # pylint: disable=undefined-variable
        result = 4 + spam * 3  # name 'spam' is not defined
        # We should not get here at all.
        # 我们根本不应该执行到这里。
        assert result
    except NameError:
        # We should get here because of division by zero.
        # 因为发生了除以零的错误，所以应该执行到这里。
        exception_has_been_handled = True

    assert exception_has_been_handled

    # A try statement may have more than one except clause, to specify handlers for different
    # exceptions. At most one handler will be executed. Handlers only handle exceptions that occur
    # in the corresponding try clause, not in other handlers of the same try statement. An except
    # clause may name multiple exceptions as a parenthesized tuple, for example:
    # 一个 try 语句可以有多个 except 子句，用来为不同的异常指定不同的处理程序。
    # 最多只会有一个处理程序被执行。处理程序只会处理对应 try 子句中发生的异常，
    # 而不会处理同一 try 语句中其他处理程序里发生的异常。一个 except 子句可以以带括号的元组
    # 形式同时指定多个异常，例如：

    exception_has_been_handled = False
    try:
        result = 10 * (1 / 0)  # division by zero
        # We should not get here at all.
        # 我们根本不应该执行到这里。
        assert result
    except (ZeroDivisionError, NameError):
        # We should get here because of division by zero.
        # 因为发生了除以零的错误，所以应该执行到这里。
        exception_has_been_handled = True

    assert exception_has_been_handled

    # Exception handlers may be chained.
    # 异常处理程序可以串联起来使用。
    exception_has_been_handled = False
    try:
        result = 10 * (1 / 0)  # division by zero
        # We should not get here at all.
        # 我们根本不应该执行到这里。
        assert result
    except NameError:
        # We should get here because of division by zero.
        # 因为发生了除以零的错误，所以应该执行到这里。
        exception_has_been_handled = True
    except ZeroDivisionError:
        # We should get here because of division by zero.
        # 因为发生了除以零的错误，所以应该执行到这里。
        exception_has_been_handled = True

    assert exception_has_been_handled

    # The try … except statement has an optional else clause, which, when present, must follow all
    # except clauses. It is useful for code that must be executed if the try clause does not raise
    # an exception. For example:
    # try … except 语句还有一个可选的 else 子句，如果存在，它必须位于所有 except 子句之后。
    # 它适用于那些只有在 try 子句没有引发异常时才需要执行的代码。例如：

    exception_has_been_handled = False
    no_exceptions_has_been_fired = False

    try:
        result = 10
        # We should not get here at all.
        # 我们根本不应该执行到这里。
        assert result
    except NameError:
        # We should get here because of division by zero.
        # 因为发生了除以零的错误，所以应该执行到这里。
        exception_has_been_handled = True
    else:
        no_exceptions_has_been_fired = True

    assert not exception_has_been_handled
    assert no_exceptions_has_been_fired
