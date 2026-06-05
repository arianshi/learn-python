"""Class Definition Syntax.

类定义语法 (Class Definition Syntax)

@see: https://docs.python.org/3/tutorial/classes.html#instance-objects
"""


def test_instance_objects():
    """Instance Objects.

    Now what can we do with instance objects? The only operations understood by instance objects
    are attribute references. There are two kinds of valid attribute names:
    - data attributes
    - methods.
    """
    # 实例对象。
    #
    # 那么我们能对实例对象做什么呢？实例对象唯一支持的操作就是属性引用。有效的属性名有
    # 两种：
    # - 数据属性 (data attributes)
    # - 方法 (methods)

    # DATA ATTRIBUTES need not be declared; like local variables, they spring into existence when
    # they are first assigned to. For example, if x is the instance of MyCounter created above,
    # the following piece of code will print the value 16, without leaving a trace.
    # 「数据属性」不需要声明；它们就像局部变量一样，第一次被赋值时就会自动出现。例如，
    # 如果 x 是上面创建的 MyCounter 的实例，下面这段代码将打印出值 16，并且不会留下
    # 任何痕迹。

    # pylint: disable=too-few-public-methods
    class DummyClass:
        """Dummy class"""
        pass

    dummy_instance = DummyClass()

    # pylint: disable=attribute-defined-outside-init
    dummy_instance.temporary_attribute = 1
    assert dummy_instance.temporary_attribute == 1
    del dummy_instance.temporary_attribute
