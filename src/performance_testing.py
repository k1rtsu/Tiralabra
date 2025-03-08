import sys
import os
from time import time
from algs.lz78 import (
    coding,
    decoding as decoding_lz,
    save_compressed as save_compressed_file_lz,
    load_compressed as load_compressed_file_lz,
)
from algs.huffman import (
    HuffmanCode,
    decoding,
    save_compressed_file,
    load_compressed_file,
)

sys.path.append(os.path.abspath("src"))
sys.path.append(os.path.abspath("data"))


def read_file(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        content = file.read()

    return content


for f in os.listdir("data/test_data"):
    file_path = os.path.join("data/test_data", f)
    print(f)
    print("Huffman")
    start_time = time()
    text = read_file(file_path)
    hf = HuffmanCode(text)
    save_compressed_file("test.bin", hf.tree(), hf.code())
    encoding_time = time()
    dc_tree, dc_code = load_compressed_file("test.bin")
    dc = decoding(dc_code, dc_tree)
    dc_time = time()
    print(True if dc == text else False)
    print(f"Encoding: {encoding_time - start_time}")
    print(f"Decoging: {dc_time - encoding_time}")
    print(f"Full performance time: {dc_time - start_time}")
    print()
    print("LZ-78")
    print(f)
    start_time = time()
    text = read_file(file_path)
    encode = coding(text)
    save_compressed_file_lz("test.bin", encode)
    encoding_time = time()
    decode = load_compressed_file_lz("test.bin")
    dc_text = decoding_lz(decode)
    dc_time = time()
    print(True if dc_text == text else False)
    print(f"Encoding: {encoding_time - start_time}")
    print(f"Decoging: {dc_time - encoding_time}")
    print(f"Full performance time: {dc_time - start_time}")
    print()
