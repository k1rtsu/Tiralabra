import sys
import os
from algs.lz78 import coding, decoding, save_compressed, load_compressed

sys.path.append(os.path.abspath("src"))
sys.path.append(os.path.abspath("data"))

def read_file(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        content = file.read()

    return content


for f in os.listdir("data/test_data"):
    print(f)
    text = read_file(f"data/test_data/{f}")
    size = os.path.getsize(f"data/test_data/{f}")

    code = coding(text)
    save_compressed("test.bin", code)
    compressed_size = os.path.getsize("test.bin")
    dc = load_compressed("test.bin")
    new_text = decoding(dc)
    print(True if new_text == text else False)

    print(
        f"Origin size: {size}    Compressed size: {compressed_size}   Compressing % {(compressed_size / size) * 100} from origin"
    )
