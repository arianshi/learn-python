"""Reading and Writing Files

读写文件 (Reading and Writing Files)

@see: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""


def test_files_open():
    """Open files

    open() returns a file object, and is most commonly used with two arguments:
    open(filename, mode).

    open() 返回一个文件对象，最常用的调用方式是带两个参数：open(filename, mode)。

    The first argument is a string containing the filename. The second argument is another string
    containing a few characters describing the way in which the file will be used. mode can be:

    - 'r' when the file will only be read,
    - 'w' for only writing (an existing file with the same name will be erased),
    - 'a' opens the file for appending; any data written to the file is automatically added to end.
    - 'r+' opens the file for both reading and writing.

    第一个参数是包含文件名的字符串。第二个参数是另一个字符串，包含若干字符，
    描述文件将以何种方式使用。mode 可以是：

    - 'r' 仅读取文件，
    - 'w' 仅写入（同名的已有文件将被清空），
    - 'a' 以追加方式打开文件；写入文件的任何数据都会自动添加到末尾。
    - 'r+' 同时打开文件用于读取和写入。

    The mode argument is optional; 'r' will be assumed if it’s omitted.

    mode 参数是可选的；如果省略，默认为 'r'。

    Normally, files are opened in text mode, that means, you read and write strings from and to the
    file, which are encoded in a specific encoding. If encoding is not specified, the default is
    platform dependent (see open()). 'b' appended to the mode opens the file in binary mode: now
    the data is read and written in the form of bytes objects. This mode should be used for all
    files that don’t contain text.

    通常情况下，文件以文本模式打开，也就是说，你从文件读取或写入字符串，这些字符串以特定的
    编码方式进行编码。如果未指定编码，则默认值取决于平台（请参阅 open()）。在 mode 后追加 'b'
    会以二进制模式打开文件：此时数据以字节对象的形式读写。这种模式应当用于所有不包含文本的文件。

    In text mode, the default when reading is to convert platform-specific line endings (\n on
    Unix, \r\n on Windows) to just \n. When writing in text mode, the default is to convert
    occurrences of \n back to platform-specific line endings. This behind-the-scenes modification
    to file data is fine for text files, but will corrupt binary data like that in JPEG or EXE
    files. Be very careful to use binary mode when reading and writing such files.

    在文本模式下，读取时默认会将平台特定的行结束符（Unix 上的 \n、Windows 上的 \r\n）转换为
    单纯的 \n。在文本模式下写入时，默认会将出现的 \n 转换回平台特定的行结束符。这种对文件
    数据的幕后修改对文本文件来说没问题，但会破坏二进制数据，例如 JPEG 或 EXE 文件中的数据。
    在读写此类文件时，请务必小心使用二进制模式。

    It is good practice to use the with keyword when dealing with file objects. The advantage is
    that the file is properly closed after its suite finishes, even if an exception is raised at
    some point. Using with is also much shorter than writing equivalent try-finally blocks:

    在处理文件对象时，使用 with 关键字是一种好的做法。其优点在于，即使在某个时刻抛出了异常，
    文件也会在其代码块结束后被正确地关闭。使用 with 也比编写等价的 try-finally 块要简短得多：
    """

    # Open files without using 'with' statement.
    # 不使用 'with' 语句打开文件。
    file = open('src/files/multi_line_file.txt', 'r')

    assert not file.closed

    read_data = file.read()

    assert read_data == (
        'first line\n'
        'second line\n'
        'third line'
    )

    file.close()

    assert file.closed

    # Open file using with.
    # 使用 with 语句打开文件。
    with open('src/files/multi_line_file.txt', 'r') as file:
        read_data = file.read()

        assert read_data == (
            'first line\n'
            'second line\n'
            'third line'
        )

    assert file.closed

    # If you’re not using the with keyword, then you should call f.close() to close the file and
    # immediately free up any system resources used by it. If you don’t explicitly close a file,
    # Python’s garbage collector will eventually destroy the object and close the open file for you,
    # but the file may stay open for a while. Another risk is that different Python implementations
    # will do this clean-up at different times.
    # 如果你没有使用 with 关键字，那么你应该调用 f.close() 来关闭文件并立即释放它所占用的
    # 系统资源。如果你没有显式地关闭文件，Python 的垃圾回收器最终会销毁该对象并替你关闭已打开
    # 的文件，但文件可能在此期间一直保持打开状态。另一个风险是，不同的 Python 实现可能会
    # 在不同的时间进行这种清理工作。
