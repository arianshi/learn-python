"""Data Compression.

数据压缩 (Data Compression)

@see: https://docs.python.org/3/tutorial/stdlib.html#data-compression

Common data archiving and compression formats are directly supported by modules including: zlib,
gzip, bz2, lzma, zipfile and tarfile.

常见的数据归档和压缩格式由多个模块直接支持，包括: zlib、gzip、bz2、lzma、zipfile 和 tarfile。
"""

import zlib


def test_zlib():
    """zlib."""
    # zlib 压缩
    string = b'witch which has which witches wrist watch'
    assert len(string) == 41

    zlib_compressed_string = zlib.compress(string)
    assert len(zlib_compressed_string) == 37

    zlib_decompressed_string = zlib.decompress(zlib_compressed_string)
    assert zlib_decompressed_string == b'witch which has which witches wrist watch'

    assert zlib.crc32(string) == 226805979
