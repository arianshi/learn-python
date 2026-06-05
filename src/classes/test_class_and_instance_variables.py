"""Class and Instance Variables.

类变量与实例变量 (Class and Instance Variables)

@see: https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables

Generally speaking, instance variables are for data unique to each instance and class variables are
for attributes and methods shared by all instances of the class.

一般来说，实例变量用于存储每个实例独有的数据，而类变量用于存储该类所有实例共享的
属性和方法。
"""


def test_class_and_instance_variables():
    """Class and Instance Variables."""
    # 类变量与实例变量

    # pylint: disable=too-few-public-methods
    class Dog:
        """Dog class example"""
        kind = 'canine'  # Class variable shared by all instances.

        def __init__(self, name):
            self.name = name  # Instance variable unique to each instance.

    fido = Dog('Fido')
    buddy = Dog('Buddy')

    # Shared by all dogs.
    # 所有狗共享。
    assert fido.kind == 'canine'
    assert buddy.kind == 'canine'

    # Unique to fido.
    # fido 独有。
    assert fido.name == 'Fido'

    # Unique to buddy.
    # buddy 独有。
    assert buddy.name == 'Buddy'

    # Shared data can have possibly surprising effects with involving mutable objects such as lists
    # and dictionaries. For example, the tricks list in the following code should not be used as a
    # class variable because just a single list would be shared by all Dog instances.
    # 当涉及到列表、字典等可变对象时，共享数据可能会产生令人意外的效果。例如，下面代码中的
    # tricks 列表不应该作为类变量使用，因为只会有一个列表被所有 Dog 实例共享。

    # pylint: disable=too-few-public-methods
    class DogWithSharedTricks:
        """Dog class example with wrong shared variable usage"""
        tricks = []  # Mistaken use of a class variable (see below) for mutable objects.

        def __init__(self, name):
            self.name = name  # Instance variable unique to each instance.

        def add_trick(self, trick):
            """Add trick to the dog

            This function illustrate mistaken use of mutable class variable tricks (see below).
            """
            # 给狗添加一个技能
            # 这个函数演示了对可变类变量 tricks 的错误使用方式（见下文）。
            self.tricks.append(trick)

    fido = DogWithSharedTricks('Fido')
    buddy = DogWithSharedTricks('Buddy')

    fido.add_trick('roll over')
    buddy.add_trick('play dead')

    assert fido.tricks == ['roll over', 'play dead']  # unexpectedly shared by all dogs
    assert buddy.tricks == ['roll over', 'play dead']  # unexpectedly shared by all dogs

    # Correct design of the class should use an instance variable instead:
    # 正确的类设计应该改用实例变量：

    # pylint: disable=too-few-public-methods
    class DogWithTricks:
        """Dog class example"""

        def __init__(self, name):
            self.name = name  # Instance variable unique to each instance.
            self.tricks = []  # creates a new empty list for each dog

        def add_trick(self, trick):
            """Add trick to the dog

            This function illustrate mistaken use of mutable class variable tricks (see below).
            """
            # 给狗添加一个技能
            # 这个函数演示了对可变类变量 tricks 的错误使用方式（见下文）。
            self.tricks.append(trick)

    fido = DogWithTricks('Fido')
    buddy = DogWithTricks('Buddy')

    fido.add_trick('roll over')
    buddy.add_trick('play dead')

    assert fido.tricks == ['roll over']
    assert buddy.tricks == ['play dead']
