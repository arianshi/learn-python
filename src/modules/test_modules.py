"""Modules.

模块 (Modules)

@see: https://docs.python.org/3/tutorial/modules.html

As your program gets longer, you may want to split it into several files for easier maintenance.
You may also want to use a handy function that you’ve written in several programs without copying
its definition into each program.

当你的程序变得越来越长时，你可能希望将其拆分为多个文件以便于维护。
你也可能希望在多个程序中使用某个已经写好的函数，而不必将其定义复制到每个程序中。

To support this, Python has a way to put definitions in a file and use them in a script or in an
interactive instance of the interpreter. Such a file is called a module; definitions from a module
can be imported into other modules or into the main module (the collection of variables that you
have access to in a script executed at the top level and in calculator mode).

为了支持这一点, Python 提供了一种方法：将定义放入一个文件中，然后在脚本或解释器的交互式
实例中使用它们。这样的文件被称为「模块」(module)；模块中的定义可以被导入到其他模块中，
或者导入到主模块中（即在顶层执行的脚本和计算器模式下可访问的变量集合）。

# 中文注解

A module is a file containing Python definitions and statements. The file name is the module name
with the suffix .py appended. Within a module, the module’s name (as a string) is available as the
value of the global variable __name__.

模块就是一个包含 Python 定义和语句的文件。文件名即模块名，后缀为 .py。在一个模块内部，
模块的名称（作为字符串）可以通过全局变量 __name__ 获得。
"""

# This does not enter the names of the functions defined in fibonacci_module directly in the
# current symbol table; it only enters the module name fibonacci_module there.
# 这种导入方式不会将 fibonacci_module 中定义的函数名直接放入当前的符号表中；
# 它只是将模块名 fibonacci_module 放入符号表。
import fibonacci_module

# There is a variant of the import statement that imports names from a module directly into the
# importing module’s symbol table. For example:
# import 语句有一种变体，它会将模块中的名称直接导入到当前模块的符号表中。例如：

# pylint: disable=reimported
from fibonacci_module import fibonacci_at_position, fibonacci_smaller_than

# There is even a variant to import all names that a module defines. This imports all names except
# those beginning with an underscore (_). In most cases Python programmers do not use this facility
# since it introduces an unknown set of names into the interpreter, possibly hiding some things you
# have already defined.
# 还有一种变体可以导入模块定义的所有名称。它会导入除了以下划线 (_) 开头之外的所有名称。
# 大多数情况下 Python 程序员不会使用这种方式，因为它会引入一组未知的名称到解释器中，
# 可能会覆盖你已经定义好的某些内容。
# >>> from fibonacci_module import *

# If the module name is followed by as, then the name following as is bound directly to the
# imported module:
# 如果模块名后面跟着 as，那么 as 后面的名称会直接绑定到所导入的模块上：
import fibonacci_module as fibonacci_module_renamed

# It can also be used when utilising from with similar effects:
# 在使用 from 时也可以采用类似的方式，效果相同：
from fibonacci_module import fibonacci_at_position as fibonacci_at_position_renamed

# When a module named spam is imported, the interpreter first searches for a built-in module with
# that name. If not found, it then searches for a file named spam.py in a list of directories
# given by the variable sys.path. sys.path is initialized from these locations:
#
# - The directory containing the input script (or the current directory when no file is specified).
# - PYTHONPATH (a list of directory names, with the same syntax as the shell variable PATH).
# - The installation-dependent default.
#
# 当导入一个名为 spam 的模块时，解释器首先会搜索同名的内置模块。如果没有找到，
# 它会在 sys.path 变量给出的目录列表中搜索名为 spam.py 的文件。
# sys.path 的初始值来自以下位置：
#
# - 包含输入脚本的目录（如果没有指定脚本，则是当前目录）。
# - PYTHONPATH（一个目录名列表，语法与 shell 变量 PATH 相同）。
# - 安装时设定的默认值。

def test_modules():
    """Modules"""
    # 模块测试

    assert fibonacci_module.fibonacci_at_position(7) == 13
    assert fibonacci_at_position(7) == 13
    assert fibonacci_module_renamed.fibonacci_at_position(7) == 13
    assert fibonacci_at_position_renamed(7) == 13

    assert fibonacci_module.fibonacci_smaller_than(100) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    assert fibonacci_smaller_than(100) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    assert fibonacci_module_renamed.fibonacci_smaller_than(10) == [0, 1, 1, 2, 3, 5, 8]

    # If you intend to use a function often you can assign it to a local name.
    # 如果你打算频繁使用某个函数，可以将它赋值给一个本地名称。
    fibonacci = fibonacci_module.fibonacci_smaller_than
    assert fibonacci(100) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    # The built-in function dir() is used to find out which names a module defines. It returns a
    # sorted list of strings.
    # 内置函数 dir() 用于查看一个模块定义了哪些名称。它返回一个排好序的字符串列表。
    assert dir(fibonacci_module) == [
        '__builtins__',
        '__cached__',
        '__doc__',
        '__file__',
        '__loader__',
        '__name__',
        '__package__',
        '__spec__',
        'fibonacci_at_position',
        'fibonacci_smaller_than',
    ]
