"""Default Argument Values

默认参数值 (Default Argument Values)

@see: https://docs.python.org/3/tutorial/controlflow.html#default-argument-values

The most useful form is to specify a default value for one or more arguments. This creates a
function that can be called with fewer arguments than it is defined to allow.

最常用的形式是为一个或多个参数指定默认值。这样创建的函数可以用比定义时所允许的更少的参数来调用。
"""


def power_of(number, power=2):
    """ Raises number to specific power.

    You may notice that by default the function raises number to the power of two.
    """
    # 将 number 提升到指定的幂次。
    # 你可能会注意到，默认情况下该函数将 number 提升到二次方。
    return number ** power


def test_default_function_arguments():
    """Test default function arguments"""
    # 测试默认函数参数

    # This function power_of can be called in several ways because it has default value for
    # the second argument. First we may call it omitting the second argument at all.
    # 由于 power_of 函数的第二个参数具有默认值，因此可以以多种方式调用它。
    # 首先，我们可以完全省略第二个参数来调用它。
    assert power_of(3) == 9
    # We may also want to override the second argument by using the following function calls.
    # 我们也可以通过以下函数调用方式来覆盖第二个参数。
    assert power_of(3, 2) == 9
    assert power_of(3, 3) == 27
