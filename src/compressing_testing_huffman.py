import sys
import os
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


def write_file(filename, data):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(data)


for f in os.listdir("data/test_data"):
    print(f)
    text = read_file(f"data/test_data/{f}")
    size = os.path.getsize(f"data/test_data/{f}")

    hc = HuffmanCode(text)
    save_compressed_file("test.bin", hc.tree(), hc.code())
    compressed_size = os.path.getsize("test.bin")
    new_tree, new_code = load_compressed_file("test.bin")
    new_text = decoding(new_code, new_tree)
    print(True if new_text == text else False)

    print(
        f"Origin size: {size}    Compressed size: {compressed_size}   Compressing % {(compressed_size / size) * 100} from origin"
    )
