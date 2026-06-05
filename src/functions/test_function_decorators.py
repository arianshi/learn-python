"""Function Decorators.

函数装饰器 (Function Decorators)

@see: https://www.thecodeship.com/patterns/guide-to-python-function-decorators/

Function decorators are simply wrappers to existing functions. In the context of design patterns,
decorators dynamically alter the functionality of a function, method or class without having to
directly use subclasses. This is ideal when you need to extend the functionality of functions that
you don't want to modify. We can implement the decorator pattern anywhere, but Python facilitates
the implementation by providing much more expressive features and syntax for that.

函数装饰器其实就是对现有函数的包装。在设计模式的语境下，装饰器可以动态地改变函数、方法或类的
功能，而无需直接使用子类。当你需要扩展某些不想修改的函数的功能时，这是非常理想的方式。
我们可以在任何地方实现装饰器模式，但 Python 通过提供更具表现力的特性和语法，使其实现更加便捷。
"""


def test_function_decorators():
    """Function Decorators."""
    # 函数装饰器。

    # Function decorators are simply wrappers to existing functions. Putting the ideas mentioned
    # above together, we can build a decorator. In this example let's consider a function that
    # wraps the string output of another function by p tags.
    # 函数装饰器其实就是对现有函数的包装。把上面提到的思想结合起来，我们就可以构建一个装饰器。
    # 在这个例子中，我们考虑一个用 p 标签包装另一个函数字符串输出的函数。

    # This is the function that we цфте to decorate.
    # 这是我们要装饰的函数。
    def greeting(name):
        return "Hello, {0}!".format(name)

    # This function decorates another functions output with <p> tag.
    # 此函数用 <p> 标签装饰另一个函数的输出。
    def decorate_with_p(func):
        def function_wrapper(name):
            return "<p>{0}</p>".format(func(name))
        return function_wrapper

    # Now, let's call our decorator and pass the function we want decorate to it.
    # 现在，让我们调用装饰器，并将我们想要装饰的函数传递给它。
    my_get_text = decorate_with_p(greeting)

    # Here we go, we've just decorated the function output without changing the function itself.
    # 就这样，我们在不修改函数本身的情况下装饰了函数的输出。
    assert my_get_text('John') == '<p>Hello, John!</p>'  # With decorator.
    assert greeting('John') == 'Hello, John!'  # Without decorator.

    # Now, Python makes creating and using decorators a bit cleaner and nicer for the programmer
    # through some syntactic sugar  There is a neat shortcut for that, which is to mention the
    # name of the decorating function before the function to be decorated. The name of the
    # decorator should be prepended with an @ symbol.
    # Python 通过一些语法糖让创建和使用装饰器对程序员来说更简洁、更友好。它提供了一个简便的快捷方式：
    # 在被装饰函数之前提及装饰器函数的名称。装饰器名称前需要加上 @ 符号。

    @decorate_with_p
    def greeting_with_p(name):
        return "Hello, {0}!".format(name)

    assert greeting_with_p('John') == '<p>Hello, John!</p>'

    # Now let's consider we wanted to decorate our greeting function by one more functions to wrap a
    # div the string output.
    # 现在假设我们想用更多的函数来装饰 greeting 函数，比如把字符串输出包裹在一个 div 中。

    # This will be our second decorator.
    # 这将是我们的第二个装饰器。
    def decorate_with_div(func):
        def function_wrapper(text):
            return "<div>{0}</div>".format(func(text))
        return function_wrapper

    # With the basic approach, decorating get_text would be along the lines of
    # greeting_with_div_p = decorate_with_div(decorate_with_p(greeting_with_p))
    # 使用基本方法，装饰 get_text 的写法会类似于：
    # greeting_with_div_p = decorate_with_div(decorate_with_p(greeting_with_p))

    # With Python's decorator syntax, same thing can be achieved with much more expressive power.
    # 使用 Python 的装饰器语法，可以用更具表现力的方式实现同样的功能。
    @decorate_with_div
    @decorate_with_p
    def greeting_with_div_p(name):
        return "Hello, {0}!".format(name)

    assert greeting_with_div_p('John') == '<div><p>Hello, John!</p></div>'

    # One important thing to notice here is that the order of setting our decorators matters.
    # If the order was different in the example above, the output would have been different.
    # 这里需要注意的一个重要事项是，装饰器的设置顺序很重要。
    # 如果在上面的例子中顺序不同，输出结果也会不同。

    # Passing arguments to decorators.
    # 给装饰器传递参数。

    # Looking back at the example before, you can notice how redundant the decorators in the
    # example are. 2 decorators(decorate_with_div, decorate_with_p) each with the same
    # functionality but wrapping the string with different tags. We can definitely do much better
    # than that. Why not have a more general implementation for one that takes the tag to wrap
    # with as a string? Yes please!
    # 回顾之前的例子，你可以注意到示例中的装饰器有多么冗余。两个装饰器
    # (decorate_with_div, decorate_with_p) 功能完全相同，只是用不同的标签包裹字符串。
    # 我们绝对可以做得更好。为什么不实现一个更通用的版本，把要包裹的标签作为字符串参数传入呢？

    def tags(tag_name):
        def tags_decorator(func):
            def func_wrapper(name):
                return "<{0}>{1}</{0}>".format(tag_name, func(name))
            return func_wrapper
        return tags_decorator

    @tags('div')
    @tags('p')
    def greeting_with_tags(name):
        return "Hello, {0}!".format(name)

    assert greeting_with_tags('John') == '<div><p>Hello, John!</p></div>'
