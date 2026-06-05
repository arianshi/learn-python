"""Methods of File Objects

文件对象的方法 (Methods of File Objects)

@see: https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects
"""


def test_file_methods():
    """Methods of File Objects"""
    # 文件对象的方法

    multi_line_file = open('src/files/multi_line_file.txt', 'r')
    binary_file = open('src/files/binary_file', 'r')

    # To read a file’s contents, call f.read(size), which reads some quantity of data and returns
    # it as a string (in text mode) or bytes object (in binary mode). size is an optional numeric
    # argument. When size is omitted or negative, the entire contents of the file will be read and
    # returned; it’s your problem if the file is twice as large as your machine’s memory. Otherwise,
    # at most size bytes are read and returned. If the end of the file has been reached, f.read()
    # will return an empty string ('').
    # 要读取文件的内容，调用 f.read(size)，它会读取一定数量的数据并将其作为字符串（在文本模式下）
    # 或字节对象（在二进制模式下）返回。size 是一个可选的数值参数。当 size 被省略或为负数时，
    # 文件的全部内容将被读取并返回；如果文件大小是你机器内存的两倍，那是你自己的问题。否则，
    # 最多读取并返回 size 个字节。如果已到达文件末尾，f.read() 将返回一个空字符串 ('')。
    read_data = multi_line_file.read()

    # pylint: disable=duplicate-code
    assert read_data == 'first line\nsecond line\nthird line'

    # To change the file object’s position, use f.seek(offset, from_what). The position is computed
    # from adding offset to a reference point; the reference point is selected by the from_what
    # argument. A from_what value of 0 measures from the beginning of the file, 1 uses the current
    # file position, and 2 uses the end of the file as the reference point. from_what can be omitted
    # and defaults to 0, using the beginning of the file as the reference point.
    # 要改变文件对象的位置，使用 f.seek(offset, from_what)。位置是通过将 offset 加到一个参考点
    # 上计算得出的；参考点由 from_what 参数选择。from_what 值为 0 表示从文件开头计算，
    # 1 表示使用当前文件位置，2 表示使用文件末尾作为参考点。from_what 可以省略，
    # 默认为 0，即使用文件开头作为参考点。
    assert binary_file.seek(0) == 0  # Go to the 0th byte in the file
    assert binary_file.seek(6) == 6  # Go to the 6th byte in the file

    assert binary_file.read(1) == '6'

    # f.readline() reads a single line from the file; a newline character (\n) is left at the end
    # of the string, and is only omitted on the last line of the file if the file doesn’t end in a
    # newline. This makes the return value unambiguous; if f.readline() returns an empty string,
    # the end of the file has been reached, while a blank line is represented by '\n', backslash n a string
    # containing only a single newline.
    # f.readline() 从文件中读取一行；字符串末尾会保留换行符 (\n)，只有在文件最后一行不以换行符
    # 结尾时才会省略。这使得返回值不会产生歧义；如果 f.readline() 返回一个空字符串，
    # 表示已到达文件末尾；而空白行则用 '\n' 表示，即只包含一个换行符的字符串。
    multi_line_file.seek(0)

    assert multi_line_file.readline() == 'first line\n'
    assert multi_line_file.readline() == 'second line\n'
    assert multi_line_file.readline() == 'third line'
    assert multi_line_file.readline() == ''

    multi_line_file.close()
    binary_file.close()
