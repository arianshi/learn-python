"""Class Definition Syntax.

类定义语法 (Class Definition Syntax)

@see: https://docs.python.org/3/tutorial/classes.html#method-objects
"""


class MyCounter:
    """A simple example of the counter class"""
    counter = 10

    def get_counter(self):
        """Return the counter"""
        # 返回计数器
        return self.counter

    def increment_counter(self):
        """Increment the counter"""
        # 让计数器自增 1
        self.counter += 1
        return self.counter


def test_method_objects():
    """Method Objects."""
    # 方法对象。

    # The other kind of instance attribute reference is a method. A method is a function that
    # “belongs to” an object. (In Python, the term method is not unique to class instances: other
    # object types can have methods as well. For example, list objects have methods called append,
    # insert, remove, sort, and so on. However, in the following discussion, we’ll use the term
    # method exclusively to mean methods of class instance objects, unless explicitly stated
    # otherwise.)
    # 另一种实例属性引用是方法 (method)。方法是"属于"某个对象的函数。（在 Python 中，
    # method 这个术语并不只用于类的实例：其他对象类型也可以有方法。例如，列表对象有
    # append、insert、remove、sort 等方法。不过，在下面的讨论中，除非另有说明，
    # 我们用 method 这个词专指类实例对象的方法。）

    # But be aware that counter.get_counter() is not the same thing as MyCounter.get_counter() —
    # it is a method object, not a function object.
    # 但要注意 counter.get_counter() 与 MyCounter.get_counter() 并不是一回事 ——
    # 前者是一个方法对象 (method object)，而不是函数对象 (function object)。

    # Usually, a method is called right after it is bound
    # 通常情况下，方法在被绑定之后会立刻被调用
    counter = MyCounter()
    assert counter.get_counter() == 10

    # However, it is not necessary to call a method right away: counter.get_counter() is a method
    # object, and can be stored away and called at a later time. For example:
    # 然而，并不一定要立刻调用方法：counter.get_counter() 是一个方法对象，可以先把它
    # 存起来，稍后再调用。例如：
    get_counter = counter.get_counter
    assert get_counter() == 10

    # What exactly happens when a method is called? You may have noticed that counter.get_counter()
    # was called without an argument above, even though the function definition for get_counter()
    # specified an argument (self). What happened to the argument? Surely Python raises an
    # exception when a function that requires an argument is called without any — even if the
    # argument isn’t actually used…
    # 当方法被调用时，到底发生了什么？你可能已经注意到，上面调用 counter.get_counter()
    # 时没有传入任何参数，尽管 get_counter() 的函数定义中指定了一个参数（self）。
    # 那个参数去哪儿了？毕竟，当一个需要参数的函数在没有传入任何参数时被调用，
    # Python 一定会抛出异常 —— 即便那个参数实际上并没有被使用……

    # Actually, you may have guessed the answer: the special thing about methods is that the
    # instance object is passed as the first argument of the function. In our example, the call
    # counter.get_counter() is exactly equivalent to MyCounter.get_counter(counter). In general,
    # calling a method with a list of n arguments is equivalent to calling the corresponding
    # function with an argument list that is created by inserting the method’s instance object
    # before the first argument.
    # 其实你可能已经猜到答案了：方法的特别之处在于，实例对象会作为函数的第一个参数
    # 被传入。在我们的例子中，counter.get_counter() 这次调用完全等价于
    # MyCounter.get_counter(counter)。一般来说，用 n 个参数调用一个方法，等价于
    # 调用对应的函数，并把方法的实例对象插到参数列表的第一个位置之前。

    assert counter.get_counter() == 10
    assert MyCounter.get_counter(counter) == 10
