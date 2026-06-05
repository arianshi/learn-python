"""Raising Exceptions.

引发异常 (Raising Exceptions)

@see: https://docs.python.org/3/tutorial/errors.html#raising-exceptions

The raise statement allows the programmer to force a specified exception to occur.

raise 语句允许程序员强制引发指定的异常。
"""


def test_raise_exception():
    """Raising Exceptions.

    The raise statement allows the programmer to force a specified exception to occur.
    """
    # 引发异常。
    # raise 语句允许程序员强制引发指定的异常。
    exception_is_caught = False

    try:
        # The sole argument to raise indicates the exception to be raised. This must be either an
        # exception instance or an exception class (a class that derives from Exception). If an
        # exception class is passed, it will be implicitly instantiated by calling its constructor
        # with no arguments
        # raise 的唯一参数表示要引发的异常。它必须是一个异常实例或一个异常类
        # (即继承自 Exception 的类)。如果传入的是异常类，将会通过调用其无参构造函数
        # 隐式地对其进行实例化。
        raise NameError('HiThere')  # shorthand for 'raise ValueError()'
    except NameError:
        exception_is_caught = True

    assert exception_is_caught


def test_user_defined_exception():
    """User-defined Exceptions"""
    # 用户自定义异常

    # Programs may name their own exceptions by creating a new exception class. Exceptions should
    # typically be derived from the Exception class, either directly or indirectly.
    # Most exceptions are defined with names that end in “Error,” similar to the naming of the
    # standard exceptions. Many standard modules define their own exceptions to report errors
    # that may occur in functions they define.
    # 程序可以通过创建一个新的异常类来命名它们自己的异常。异常通常应该直接或间接地继承自
    # Exception 类。
    # 大多数异常的命名都以「Error」结尾，类似于标准异常的命名方式。许多标准模块会定义它们
    # 自己的异常，用来报告其内部函数中可能发生的错误。
    class MyCustomError(Exception):
        """Example of MyCustomError exception."""
        # MyCustomError 异常的示例。
        def __init__(self, message):
            super().__init__(message)
            self.message = message

    custom_exception_is_caught = False

    try:
        raise MyCustomError('My custom message')
    except MyCustomError:
        custom_exception_is_caught = True

    assert custom_exception_is_caught
