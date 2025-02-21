import unittest
import sys
import os
import ast

sys.path.append(os.path.abspath("src"))

from algs.lz78 import coding, decoding, save_compressed, load_compressed


def read_file(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        content = file.read()
    return content


class TestLZ78(unittest.TestCase):
    def test_coding(self):
        word = "abracadabra"
        code = coding(word)
        answer = [(0, "a"), (0, "b"), (0, "r"), (1, "c"), (1, "d"), (1, "b"), (3, "a")]
        self.assertEqual(answer, code)

    def test_decoding(self):
        word = "abracadabra"
        code = coding(word)
        decode = decoding(code)
        self.assertEqual(decode, word)

    def test_large_text(self):
        text = read_file("data/compressing_test_data/rc.txt")
        compressed_code = coding(text)
        decode = decoding(compressed_code)
        self.assertEqual(text, decode, "The contents of the data are not the same!")

    def test_zeroredundancy_text(self):
        text = read_file("data/compressing_test_data/redundancy_zero.txt")
        compressed_code = coding(text)
        decode = decoding(compressed_code)
        self.assertEqual(text, decode, "The contents of the data are not the same!")

    def test_loremipsum_text(self):
        text = read_file("data/compressing_test_data/loremipsum.txt")
        compressed_code = coding(text)
        decode = decoding(compressed_code)
        self.assertEqual(text, decode, "The contents of the data are not the same!")

    def test_save_and_load_compressed(self):
        word = "abracadabraa"
        code = coding(word)
        save_compressed("test_compress.bin", code)
        new_code = load_compressed("test_compress.bin")
        new_word = decoding(new_code)
        self.assertEqual(new_word, word)
        os.remove("test_compress.bin")  # Cleanup after test

    def test_save_and_load_large_text_from_file(self):
        text = read_file("data/compressing_test_data/rc.txt")
        compressed_code = coding(text)
        filename = "test_large_compressed.bin"

        save_compressed(filename, compressed_code)
        loaded_code = load_compressed(filename)

        self.assertEqual(
            compressed_code,
            loaded_code,
            "Compressed data does not match after saving and loading!",
        )

        decode = decoding(loaded_code)
        self.assertEqual(text, decode, "Decompressed text does not match original!")

        os.remove(filename)  # Cleanup after test


if __name__ == "__main__":
    unittest.main()
