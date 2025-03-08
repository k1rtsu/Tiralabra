import struct
from bitarray import bitarray

"""
LZ78 Data Compression Algorithm

This module implements the LZ78 compression and decompression algorithms,
as well as functions to save and load compressed data efficiently.
"""


def coding(w: str):
    """
    Compresses the input string using the LZ78 algorithm.
    Returns a list of (index, character) tuples.
    """
    if not w:
        return []
    dictionary = {}
    compressed = []

    dict_index = 1
    char = ""
    for c in w:
        if char + c in dictionary:
            char += c
        else:
            index = dictionary.get(char, 0)
            compressed.append((index, c))
            dictionary[char + c] = dict_index
            dict_index += 1
            char = ""

    if char:
        last_char = char[-1]
        other_char = char[:-1]
        index = dictionary.get(other_char, 0)
        compressed.append((index, last_char))

    return compressed


def decoding(code: list):
    """
    Decompresses a list of (index, character) tuples to reconstruct the original string.
    """
    if not code:
        return ""
    dictionary = {}
    decompressed = ""

    dict_index = 1
    for index, char in code:
        if index == 0:
            dictionary[dict_index] = char
            decompressed += char
        else:
            decompressed += dictionary[index] + char
            dictionary[dict_index] = dictionary[index] + char
        dict_index += 1

    return decompressed


def save_compressed(filename: str, compressed_data: list):
    """
    Saves the compressed data to a binary file with optimized bit lengths.
    """
    max_index = max(idx for idx, _ in compressed_data)
    max_char = max(ord(char) for _, char in compressed_data)

    index_bits = (
        4
        if max_index < 16
        else 8 if max_index < 256 else 16 if max_index < 65536 else 32
    )

    char_bits = 8 if max_char < 256 else 16 if max_char < 65536 else 32

    with open(filename, "wb") as f:
        f.write(struct.pack("BB", index_bits, char_bits))
        bit_stream = bitarray()

        for index, char in compressed_data:
            index_bits_str = bin(index)[2:].zfill(index_bits)
            char_bits_str = bin(ord(char))[2:].zfill(char_bits)
            bit_stream.extend(index_bits_str + char_bits_str)

        bit_stream.tofile(f)


def load_compressed(filename: str):
    """
    Loads compressed data from a binary file and reconstructs the list of (index, character) tuples.
    """
    compressed_data = []

    with open(filename, "rb") as f:
        index_bits, char_bits = struct.unpack("BB", f.read(2))
        bit_stream = bitarray()
        bit_stream.fromfile(f)
        bits = bit_stream.to01()

        chunk_size = index_bits + char_bits
        bits = bits[: len(bits) - (len(bits) % chunk_size)]

        for i in range(0, len(bits), chunk_size):
            index = int(bits[i : i + index_bits], 2)
            char = chr(int(bits[i + index_bits : i + chunk_size], 2))
            compressed_data.append((index, char))

    return compressed_data
