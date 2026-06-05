"""Fibonacci numbers module.

斐波那契数列模块 (Fibonacci numbers module)

@see: https://docs.python.org/3/tutorial/modules.html

A module is a file containing Python definitions and statements. The file name is the module name
with the suffix .py appended. Within a module, the module’s name (as a string) is available as the
value of the global variable __name__.

模块就是一个包含 Python 定义和语句的文件。文件名即模块名，后缀为 .py。在一个模块内部，
模块的名称（作为字符串）可以通过全局变量 __name__ 获得。
"""


def fibonacci_at_position(position):
    """Return Fibonacci number at specified position"""
    # 返回指定位置上的斐波那契数
    current_position = 0
    previous_number, current_number = 0, 1
    while current_position < position:
        current_position += 1
        previous_number, current_number = current_number, previous_number + current_number
    return previous_number


def fibonacci_smaller_than(limit):
    """Return Fibonacci series up to limit"""
    # 返回小于 limit 的斐波那契数列
    result = []
    previous_number, current_number = 0, 1
    while previous_number < limit:
        result.append(previous_number)
        previous_number, current_number = current_number, previous_number + current_number
    return result


# When you run a Python module with:
#
# >>> python fibonacci.py <arguments>
#
# the code in the module will be executed, just as if you imported it, but with
# the __name__ set to "__main__". That means that by adding this code at the end of your module
# you can make the file usable as a script as well as an importable module, because the code that
# parses the command line only runs if the module is executed as the “main” file:
#
# >>> python fibonacci.py 50
#
# 当你使用如下方式运行一个 Python 模块时：
#
# >>> python fibonacci.py <参数>
#
# 模块中的代码会被执行，就像被导入一样，但 __name__ 会被设置为 "__main__"。这意味着
# 在模块末尾添加这段代码后，文件既可以作为可导入的模块使用，也可以作为脚本运行，
# 因为解析命令行的代码只有在模块作为「主文件」执行时才会运行：
#
# >>> python fibonacci.py 50
if __name__ == '__main__':
    import sys
    print(fibonacci_smaller_than(int(sys.argv[1])))
