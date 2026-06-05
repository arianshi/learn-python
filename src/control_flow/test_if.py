"""IF statement

IF 语句 (IF statement)

@see: https://docs.python.org/3/tutorial/controlflow.html

There can be zero or more elif parts, and the else part is optional. The keyword ‘elif’ is
short for ‘else if’, and is useful to avoid excessive indentation.

elif 部分可以有零个或多个，else 部分是可选的。关键字 'elif' 是 'else if' 的缩写，
使用它有助于避免过深的缩进。

An if … elif … elif … sequence is a substitute for the switch or case statements found
in other languages.

if … elif … elif … 这样的序列可以替代其他语言中的 switch 或 case 语句。
"""


def test_if_statement():
    """IF statement"""
    # IF 语句

    number = 15
    conclusion = ''

    if number < 0:
        conclusion = 'Number is less than zero'
    elif number == 0:
        conclusion = 'Number equals to zero'
    elif number < 1:
        conclusion = 'Number is greater than zero but less than one'
    else:
        conclusion = 'Number bigger than or equal to one'

    assert conclusion == 'Number bigger than or equal to one'
