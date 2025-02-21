# The LZ78 algorithm is a data compression algorithm developed in 1978.
# The algorithm compresses data by replacing repeated strings with shorter symbols.
# It is also efficient because it does not require a separate dictionary; instead, it creates the dictionary while compressing the data.
import struct
from bitarray import bitarray


def coding(w: str):
    """
    Compresses the input string using the LZ78 algorithm.
    Returns a list of (index, character) tuples.
    """
    if w == "":
        return []
    dictionary = {}
    compressed = []

    dict_index = 1
    char = ""
    for i in range(len(w)):
        if char + w[i] in dictionary:
            char += w[i]

        else:
            index = dictionary.get(char, 0)
            compressed.append((index, w[i]))
            dictionary[char + w[i]] = dict_index
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
    if code == []:
        return ""
    dicttionary = {}
    decompressed = ""

    dict_index = 1
    for i in code:
        if i[0] == 0:
            dicttionary[dict_index] = i[1]
            decompressed += i[1]
            dict_index += 1

        else:
            decompressed += dicttionary[i[0]] + i[1]
            dicttionary[dict_index] = dicttionary[i[0]] + i[1]
            dict_index += 1

    return decompressed


def save_compressed(filename: str, compressed_data: list):
    """
    Saves the compressed data to a binary file with optimized bit lengths.
    """

    max_index = max(idx for idx, _ in compressed_data)
    max_char = max(ord(char) for _, char in compressed_data)

    # Valitse indeksille bittimäärä
    if max_index < 16:
        index_bits = 4
    elif max_index < 256:
        index_bits = 8
    elif max_index < 65536:
        index_bits = 16
    else:
        index_bits = 32

    # Valitse merkille bittimäärä
    if max_char < 256:
        char_bits = 8
    elif max_char < 65536:
        char_bits = 16
    else:
        char_bits = 32

    with open(filename, "wb") as f:
        f.write(
            struct.pack("BB", index_bits, char_bits)
        )  # Tallennetaan bittimäärät 1 tavuna kumpikin
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
        index_bits, char_bits = struct.unpack(
            "BB", f.read(2)
        )  # Luetaan indeksin ja merkin bittimäärät
        bit_stream = bitarray()
        bit_stream.fromfile(f)
        bits = bit_stream.to01()

        chunk_size = index_bits + char_bits  # Indeksi + merkki

        if len(bits) % chunk_size != 0:
            raise ValueError("Tiedoston koko ei täsmää odotettuun bittijakoon")

        for i in range(0, len(bits), chunk_size):
            index = int(bits[i : i + index_bits], 2)
            char = chr(int(bits[i + index_bits : i + chunk_size], 2))
            compressed_data.append((index, char))

    return compressed_data
