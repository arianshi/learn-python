"""String Pattern Matching.

字符串模式匹配 (String Pattern Matching)

@see: https://docs.python.org/3/tutorial/stdlib.html#string-pattern-matching

The re module provides regular expression tools for advanced string processing.
For complex matching and manipulation, regular expressions offer succinct, optimized solutions:

re 模块提供了用于高级字符串处理的正则表达式工具。
对于复杂的匹配和操作，正则表达式提供了简洁且优化的解决方案：
"""

import re


def test_re():
    """String Pattern Matching"""
    # 字符串模式匹配

    assert re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest') == [
        'foot',
        'fell',
        'fastest'
    ]

    assert re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat') == 'cat in the hat'

    # When only simple capabilities are needed, string methods are preferred because they are
    # easier to read and debug:
    # 当只需要简单功能时，更推荐使用字符串方法，因为它们更易于阅读和调试：
    assert 'tea for too'.replace('too', 'two') == 'tea for two'
