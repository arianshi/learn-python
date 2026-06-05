"""Variables

变量 (Variables)

@see: https://docs.python.org/3/tutorial/introduction.html
@see: https://www.w3schools.com/python/python_variables.asp
@see: https://www.learnpython.org/en/Variables_and_Types

Python is completely object oriented, and not "statically typed".
You do not need to declare variables before using them, or declare
their type. Every variable in Python is an object.

Python 是完全面向对象的语言，并且不是“静态类型”的。
你不需要在使用变量之前声明变量或声明它们的类型。
Python 中的每个变量都是一个对象。

Unlike other programming languages, Python has no command for
declaring a variable. A variable is created the moment you first assign
a value to it.

与其他编程语言不同，Python 没有用于声明变量的命令。
变量是在你第一次为它赋值时创建的。

A variable can have a short name (like x and y) or a more descriptive name
(age, carname, total_volume).

变量可以有一个简短的名字（如 x 和 y），也可以有一个更具描述性的名字
（如 age、carname、total_volume）。

Rules for Python variables:
- A variable name must start with a letter or the underscore character.
- A variable name cannot start with a number.
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ).
- Variable names are case-sensitive (age, Age and AGE are three different variables).

Python 变量命名规则：
- 变量名必须以字母或下划线字符开头。
- 变量名不能以数字开头。
- 变量名只能包含字母数字字符和下划线（A-z、0-9 和 _ ）。
- 变量名是区分大小写的（age、Age 和 AGE 是三个不同的变量）。
"""


def test_variables():
    """Test variables"""
    # 测试变量

    integer_variable = 5
    string_variable = 'John'

    assert integer_variable == 5
    assert string_variable == 'John'

    variable_with_changed_type = 4  # x is of type int
    variable_with_changed_type = 'Sally'  # x is now of type str

    assert variable_with_changed_type == 'Sally'
