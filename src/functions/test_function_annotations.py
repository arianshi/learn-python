"""Function Annotations.

函数注解 (Function Annotations)

@see: https://docs.python.org/3/tutorial/controlflow.html#function-annotations

Function annotations are completely optional metadata information about the types used
by user-defined functions.

函数注解是关于用户定义函数所使用的类型的完全可选的元数据信息。

Annotations are stored in the __annotations__ attribute of the function as a dictionary and have no
effect on any other part of the function. Parameter annotations are defined by a colon after the
parameter name, followed by an expression evaluating to the value of the annotation. Return
annotations are defined by a literal ->, followed by an expression, between the parameter list and
the colon denoting the end of the def statement.

注解以字典的形式存储在函数的 __annotations__ 属性中，对函数的其他任何部分都没有影响。
参数注解的定义方式是在参数名后加上冒号，然后跟一个表达式（其值即注解的值）。返回值注解的
定义方式是在参数列表后面、表示 def 语句结束的冒号之前，使用字面量 -> 后跟一个表达式。
"""


def breakfast(ham: str, eggs: str = 'eggs') -> str:
    """Breakfast creator.

    This function has a positional argument, a keyword argument, and the return value annotated.
    """
    # 早餐生成器。
    # 此函数对位置参数、关键字参数和返回值都进行了注解。
    return ham + ' and ' + eggs


def test_function_annotations():
    """Function Annotations."""
    # 函数注解测试。

    assert breakfast.__annotations__ == {'eggs': str, 'ham': str, 'return': str}
