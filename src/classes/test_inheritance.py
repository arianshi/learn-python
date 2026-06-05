"""Inheritance

继承 (Inheritance)

@see: https://docs.python.org/3/tutorial/classes.html#inheritance
"""


# pylint: disable=too-few-public-methods
class Person:
    """Example of the base class"""
    def __init__(self, name):
        self.name = name

    def get_name(self):
        """Get person name"""
        # 获取人名
        return self.name


# The syntax for a derived class definition looks like this.
# 派生类定义的语法如下所示。
# pylint: disable=too-few-public-methods
class Employee(Person):
    """Example of the derived class

    The Base Class (in our case Person) must be defined in a scope containing the derived class
    definition. In place of a base class name, other arbitrary expressions are also allowed.

    Derived classes may override methods of their base classes. Because methods have no special
    privileges when calling other methods of the same object, a method of a base class that calls
    another method defined in the same base class may end up calling a method of a derived class
    that overrides it.

    An overriding method in a derived class may in fact want to extend rather than simply replace
    the base class method of the same name. There is a simple way to call the base class method
    directly: just call BaseClassName.methodname(self, arguments). This is occasionally useful to
    clients as well. (Note that this only works if the base class is accessible as BaseClassName
    in the global scope.)
    """
    def __init__(self, name, staff_id):
        Person.__init__(self, name)
        # You may also use super() here in order to avoid explicit using of parent class name:
        # 你也可以在这里使用 super() 来避免显式地写出父类的名称：
        # >>> super().__init__(name)
        self.staff_id = staff_id

    def get_full_id(self):
        """Get full employee id"""
        # 获取员工的完整 id
        return self.get_name() + ', ' + self.staff_id


def test_inheritance():
    """Inheritance."""
    # 继承

    # There’s nothing special about instantiation of derived classes: DerivedClassName() creates a
    # new instance of the class. Method references are resolved as follows: the corresponding class
    # attribute is searched, descending down the chain of base classes if necessary, and the method
    # reference is valid if this yields a function object.
    # 派生类的实例化没有什么特别的：DerivedClassName() 会创建该类的一个新实例。方法引用
    # 是这样解析的：搜索对应的类属性，必要时会沿着基类链向下搜索；如果最终得到一个函数
    # 对象，那么该方法引用就是有效的。
    person = Person('Bill')
    employee = Employee('John', 'A23')

    assert person.get_name() == 'Bill'
    assert employee.get_name() == 'John'
    assert employee.get_full_id() == 'John, A23'

    # Python has two built-in functions that work with inheritance:
    #
    # - Use isinstance() to check an instance’s type: isinstance(obj, int) will be True only if
    # obj.__class__ is int or some class derived from int.
    #
    # - Use issubclass() to check class inheritance: issubclass(bool, int) is True since bool is
    # a subclass of int. However, issubclass(float, int) is False since float is not a subclass
    # of int.
    # Python 有两个与继承相关的内置函数：
    #
    # - 使用 isinstance() 来检查一个实例的类型：只有当 obj.__class__ 是 int 或者
    # 从 int 派生而来的某个类时，isinstance(obj, int) 才会为 True。
    #
    # - 使用 issubclass() 来检查类的继承关系：issubclass(bool, int) 为 True，因为
    # bool 是 int 的子类。但是 issubclass(float, int) 为 False，因为 float 不是
    # int 的子类。

    assert isinstance(employee, Employee)
    assert not isinstance(person, Employee)

    assert isinstance(person, Person)
    assert isinstance(employee, Person)

    assert issubclass(Employee, Person)
    assert not issubclass(Person, Employee)
