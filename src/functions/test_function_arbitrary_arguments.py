"""Arbitrary Argument Lists

任意参数列表 (Arbitrary Argument Lists)

@see: https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists

Function can be called with an arbitrary number of arguments. These arguments will be wrapped up in
a tuple. Before the variable number of arguments, zero or more normal arguments may occur.

函数可以被调用时传入任意数量的参数。这些参数会被包装成一个元组。在可变数量的参数之前，
可以有零个或多个普通参数。
"""


def test_function_arbitrary_arguments():
    """Arbitrary Argument Lists"""
    # 任意参数列表

    # When a final formal parameter of the form **name is present, it receives a dictionary
    # containing all keyword arguments except for those corresponding to a formal parameter.
    # This may be combined with a formal parameter of the form *name which receives a tuple
    # containing the positional arguments beyond the formal parameter list.
    # (*name must occur before **name.) For example, if we define a function like this:
    # 当最后一个形参为 **name 的形式时，它会接收一个字典，其中包含除了已经对应于某个形参的
    # 关键字参数之外的所有关键字参数。它可以与 *name 形式的形参组合使用，*name 会接收一个元组，
    # 其中包含超出形参列表之外的位置参数。
    # （*name 必须出现在 **name 之前。）例如，如果我们这样定义一个函数：
    def test_function(first_param, *arguments):
        """This function accepts its arguments through "arguments" tuple amd keywords dictionary."""
        # 此函数通过 "arguments" 元组和关键字字典接收其参数。
        assert first_param == 'first param'
        assert arguments == ('second param', 'third param')

    test_function('first param', 'second param', 'third param')

    # Normally, these variadic arguments will be last in the list of formal parameters, because
    # they scoop up all remaining input arguments that are passed to the function. Any formal
    # parameters which occur after the *args parameter are ‘keyword-only’ arguments, meaning that
    # they can only be used as keywords rather than positional arguments.
    # 通常，这些可变参数会出现在形参列表的最后，因为它们会收集所有传递给函数的剩余输入参数。
    # 任何出现在 *args 参数之后的形参都是「仅关键字」参数，这意味着它们只能作为关键字使用，
    # 而不能作为位置参数使用。
    def concat(*args, sep='/'):
        return sep.join(args)

    assert concat('earth', 'mars', 'venus') == 'earth/mars/venus'
    assert concat('earth', 'mars', 'venus', sep='.') == 'earth.mars.venus'
