"""Class Definition Syntax.

类定义语法 (Class Definition Syntax)

@see: https://docs.python.org/3/tutorial/classes.html

Python is an object oriented programming language.
Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects.

Python 是一种面向对象的编程语言。
Python 中几乎所有的东西都是对象，都有其属性和方法。
类就像一个对象构造器，或者说是用于创建对象的"蓝图"。
"""


def test_class_definition():
    """Class definition."""
    # 类定义

    # Class definitions, like function definitions (def statements) must be executed before they
    # have any effect. (You could conceivably place a class definition in a branch of an if
    # statement, or inside a function.)
    # 类定义和函数定义（def 语句）一样，必须先被执行才会生效。
    # （你完全可以把类定义放在 if 语句的某个分支里，或者放在某个函数内部。）

    class GreetingClass:
        """Example of the class definition

        This class contains two public methods and doesn't contain constructor.
        """
        name = 'user'

        def say_hello(self):
            """Class method."""
            # 类方法。
            # The self parameter is a reference to the class itself, and is used to access variables
            # that belongs to the class. It does not have to be named self , you can call it
            # whatever you like, but it has to be the first parameter of any function in the class.
            # self 参数是对类自身的引用，用于访问属于该类的变量。它不一定要叫 self，你可以
            # 给它起任何名字，但它必须是类中任何函数的第一个参数。
            return 'Hello ' + self.name

        def say_goodbye(self):
            """Class method."""
            # 类方法。
            return 'Goodbye ' + self.name

    # When a class definition is entered, a new namespace is created, and used as the local scope —
    # thus, all assignments to local variables go into this new namespace. In particular, function
    # definitions bind the name of the new function here.
    # 进入类定义时，会创建一个新的命名空间，并将其用作局部作用域 —— 因此，所有对局部
    # 变量的赋值都会进入这个新的命名空间。特别是，函数定义会在这里绑定新函数的名称。

    # Class instantiation uses function notation. Just pretend that the class object is a
    # parameterless function that returns a new instance of the class. For example the following
    # code will creates a new instance of the class and assigns this object to the local variable.
    # 类的实例化使用函数调用的语法。就当类对象是一个无参函数，它返回该类的一个新实例。
    # 例如下面的代码会创建该类的一个新实例并将该对象赋值给本地变量。
    greeter = GreetingClass()

    assert greeter.say_hello() == 'Hello user'
    assert greeter.say_goodbye() == 'Goodbye user'
