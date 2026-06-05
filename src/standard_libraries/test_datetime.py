"""Dates and Times.

日期和时间 (Dates and Times)

@see: https://docs.python.org/3/tutorial/stdlib.html#dates-and-times

The datetime module supplies classes for manipulating dates and times in both simple and complex
ways. While date and time arithmetic is supported, the focus of the implementation is on efficient
member extraction for output formatting and manipulation. The module also supports objects that
are timezone aware.

datetime 模块提供了用于以简单或复杂方式操作日期和时间的类。
虽然支持日期和时间的算术运算，但实现的重点在于高效地提取成员以用于
输出格式化和操作。该模块还支持时区感知的对象。
"""

from datetime import date


def test_datetime():
    """Dates and Times"""
    # 日期和时间

    real_now = date.today()
    assert real_now

    fake_now = date(2018, 8, 29)

    assert fake_now.day == 29
    assert fake_now.month == 8
    assert fake_now.year == 2018
    assert fake_now.ctime() == 'Wed Aug 29 00:00:00 2018'
    assert fake_now.strftime(
        '%m-%d-%y. %d %b %Y is a %A on the %d day of %B.'
    ) == '08-29-18. 29 Aug 2018 is a Wednesday on the 29 day of August.'

    # Dates support calendar arithmetic.
    # 日期支持日历算术运算。
    birthday = date(1964, 7, 31)
    age = fake_now - birthday

    assert age.days == 19752
