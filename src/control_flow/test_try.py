"""TRY statement

TRY 语句 (TRY statement)

@see: https://www.w3schools.com/python/python_try_except.asp

"try" statement is used for exception handling.
When an error occurs, or exception as we call it, Python will normally stop and generate an error
message. These exceptions can be handled using the try statement.

"try" 语句用于异常处理。
当发生错误（也就是我们所说的异常）时，Python 通常会停止运行并生成一条错误信息。
这些异常可以通过 try 语句来处理。

The "try" block lets you test a block of code for errors.
The "except" block lets you handle the error.
The "else" block lets you execute the code if no errors were raised.
The "finally" block lets you execute code, regardless of the result of the try- and except blocks.

"try" 代码块用于测试一段代码是否有错误。
"except" 代码块用于处理错误。
"else" 代码块用于在没有发生错误时执行代码。
"finally" 代码块用于无论 try 和 except 代码块的结果如何都会被执行的代码。
"""


def test_try():
    """TRY statement"""
    # TRY 语句

    # The try block will generate an error, because x is not defined:
    # try 代码块会产生一个错误，因为 x 没有被定义：
    exception_has_been_caught = False
    # pylint: disable=bare-except
    try:
        # pylint: disable=undefined-variable
        print(not_existing_variable)
    except:
        exception_has_been_caught = True

    assert exception_has_been_caught

    # You can define as many exception blocks as you want, e.g. if you want to execute a special
    # block of code for a special kind of error:
    # 你可以定义任意多个 except 代码块，例如如果你想为某种特定类型的错误执行特定的代码块：
    exception_message = ''

    # pylint: disable=bare-except
    try:
        # pylint: disable=undefined-variable
        print(not_existing_variable)
    except NameError:
        exception_message = 'Variable is not defined'
    except:
        exception_message = 'Something else went wrong'

    assert exception_message == 'Variable is not defined'

    # You can use the else keyword to define a block of code to be executed
    # if no errors were raised.
    # 你可以使用 else 关键字定义一个代码块，它会在没有引发任何错误时被执行。
    message = ''
    try:
        message += 'Success.'
    except:
        message += 'Something went wrong.'
    else:
        message += 'Nothing went wrong.'

    assert message == 'Success.Nothing went wrong.'

    # The finally block, if specified, will be executed regardless if the try block raises an
    # error or not.
    # 如果指定了 finally 代码块，无论 try 代码块是否引发错误，它都会被执行。
    message = ''
    try:
        # pylint: disable=undefined-variable
        print(not_existing_variable)
    except:
        message += 'Something went wrong.'
    finally:
        message += 'The "try except" is finished.'

    assert message == 'Something went wrong.The "try except" is finished.'
