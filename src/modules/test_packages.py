"""Packages.

包 (Packages)

@see: https://docs.python.org/3/tutorial/modules.html#packages

Packages are a way of structuring Python’s module namespace by using “dotted module names”. For
example, the module name A.B designates a submodule named B in a package named A. Just like the
use of modules saves the authors of different modules from having to worry about each other’s
global variable names, the use of dotted module names saves the authors of multi-module packages
like NumPy or Pillow from having to worry about each other’s module names.

包是一种通过使用「点分模块名」(dotted module names) 来组织 Python 模块命名空间的方式。
例如，模块名 A.B 表示在名为 A 的包中有一个名为 B 的子模块。就像使用模块能让不同模块的
作者不必担心彼此的全局变量名一样，使用点分模块名也让 NumPy 或 Pillow 这类多模块包的
作者不必担心彼此的模块名冲突。

The __init__.py files are required to make Python treat the directories as containing packages;
this is done to prevent directories with a common name, such as string, from unintentionally hiding
valid modules that occur later on the module search path. In the simplest case, __init__.py can
just be an empty file, but it can also execute initialization code for the package or set the
__all__ variable, described later.

必须存在 __init__.py 文件，Python 才会将目录视为「包」；这样做是为了避免一些常见名称
（例如 string）的目录无意中隐藏后续搜索路径上的有效模块。最简单的情况下，__init__.py
可以是一个空文件，但它也可以执行包的初始化代码，或设置稍后会介绍的 __all__ 变量。
"""

# The __init__.py files are required to make Python treat the directories as containing packages;
# this is done to prevent directories with a common name, such as string, from unintentionally
# hiding valid modules that occur later on the module search path. In the simplest case,
# __init__.py can just be an empty file, but it can also execute initialization code for the
# package or set the __all__ variable, described later.
# 必须存在 __init__.py 文件，Python 才会将目录视为「包」；这样做是为了避免一些常见名称
# （例如 string）的目录无意中隐藏后续模块搜索路径上的有效模块。最简单的情况下，
# __init__.py 可以是一个空文件，但它也可以执行包的初始化代码，或设置稍后会介绍的
# __all__ 变量。

# Users of the package can import individual modules from the package, for example.
# 包的使用者可以从包中导入单独的模块，例如：
import sound_package.effects.echo

# An alternative way of importing the submodule is:
# 另一种导入子模块的方式是：

# pylint: disable=reimported
from sound_package.effects import echo

# Yet another variation is to import the desired function or variable directly:
# 还有一种变体是直接导入所需的函数或变量：
from sound_package.effects.echo import echo_function

# Note that when using from package import item, the item can be either a submodule (or subpackage)
# of the package, or some other name defined in the package, like a function, class or variable.
# The import statement first tests whether the item is defined in the package; if not, it assumes
# it is a module and attempts to load it. If it fails to find it, an ImportError exception is
# raised.
# 注意，当使用 `from package import item` 时，item 可以是包的子模块（或子包），也可以是
# 包中定义的其他名称，比如函数、类或变量。import 语句会先检测 item 是否在包中已定义；
# 如果没有，它会假定 item 是一个模块并尝试加载。如果仍然找不到，就会抛出 ImportError 异常。

# Contrarily, when using syntax like import item.subitem.subsubitem, each item except for the last
# must be a package; the last item can be a module or a package but can’t be a class or function or
# variable defined in the previous item.
# 相反，当使用 `import item.subitem.subsubitem` 这种语法时，除了最后一个之外，每一项都必须
# 是包；最后一项可以是模块或包，但不能是前一项中定义的类、函数或变量。


def test_packages():
    """Packages."""
    # 包测试
    assert sound_package.effects.echo.echo_function() == 'Do echo effect'
    assert echo.echo_function() == 'Do echo effect'
    assert echo_function() == 'Do echo effect'
