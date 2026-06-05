"""Class Definition Syntax.

类定义语法 (Class Definition Syntax)

@see: https://docs.python.org/3/tutorial/classes.html#class-objects
"""


def test_class_objects():
    """Class Objects.

    Class objects support two kinds of operations:
    - attribute references
    - instantiation.
    """
    # 类对象。
    #
    # 类对象支持两种操作：
    # - 属性引用 (attribute references)
    # - 实例化 (instantiation)

    # ATTRIBUTE REFERENCES use the standard syntax used for all attribute references in
    # Python: obj.name. Valid attribute names are all the names that were in the class’s namespace
    # when the class object was created. For class MyCounter the following references are valid
    # attribute references:
    # 「属性引用」使用 Python 中所有属性引用的标准语法：obj.name。有效的属性名是创建
    # 类对象时位于该类命名空间内的所有名称。对于类 MyCounter，下面这些引用都是有效的
    # 属性引用：

    class ComplexNumber:
        """Example of the complex numbers class"""

        real = 0
        imaginary = 0

        def get_real(self):
            """Return real part of complex number."""
            # 返回复数的实部。
            return self.real

        def get_imaginary(self):
            """Return imaginary part of complex number."""
            # 返回复数的虚部。
            return self.imaginary

    assert ComplexNumber.real == 0

    # __doc__ is also a valid attribute, returning the docstring belonging to the class
    # __doc__ 也是一个有效的属性，返回属于该类的文档字符串
    assert ComplexNumber.__doc__ == 'Example of the complex numbers class'

    # Class attributes can also be assigned to, so you can change the value of
    # ComplexNumber.counter by assignment.
    # 类属性也可以被赋值，因此你可以通过赋值来改变 ComplexNumber.counter 的值。
    ComplexNumber.real = 10
    assert ComplexNumber.real == 10

    # CLASS INSTANTIATION uses function notation. Just pretend that the class object is a
    # parameterless function that returns a new instance of the class. For example
    # (assuming the above class):
    # 「类的实例化」使用函数调用的语法。就当类对象是一个无参函数，它返回该类的一个新实例。
    # 例如（假设有上面定义的类）：
    complex_number = ComplexNumber()

    assert complex_number.real == 10
    assert complex_number.get_real() == 10

    # Let's change counter default value back.
    # 让我们把 counter 的默认值改回来。
    ComplexNumber.real = 10
    assert ComplexNumber.real == 10

    # The instantiation operation (“calling” a class object) creates an empty object. Many classes
    # like to create objects with instances customized to a specific initial state. Therefore a
    # class may define a special method named __init__(), like this:
    # 实例化操作（"调用"一个类对象）会创建一个空对象。许多类希望创建处于特定初始状态的
    # 实例对象。因此，一个类可以定义一个名为 __init__() 的特殊方法，如下所示：

    class ComplexNumberWithConstructor:
        """Example of the class with constructor"""
        def __init__(self, real_part, imaginary_part):
            self.real = real_part
            self.imaginary = imaginary_part

        def get_real(self):
            """Return real part of complex number."""
            # 返回复数的实部。
            return self.real

        def get_imaginary(self):
            """Return imaginary part of complex number."""
            # 返回复数的虚部。
            return self.imaginary

    complex_number = ComplexNumberWithConstructor(3.0, -4.5)
    assert complex_number.real, complex_number.imaginary == (3.0, -4.5)
