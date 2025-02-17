import unittest
import sys
import os
import ast

sys.path.append(os.path.abspath("src"))

from algs.lz78 import coding, decoding


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
        text = read_file("data/rc.txt")
        compressed_code = coding(text)
        decode = decoding(compressed_code)

        self.assertEqual(text, decode, "The contents of the data are not the same!")

    def test_empty_text(self):
        text = read_file("data/empty.txt")
        compressed_code = coding(text)

        decode = decoding(compressed_code)

        self.assertEqual(text, decode, "The contents of the data are not the same!")

    def test_zeroredundancy_text(self):
        text = read_file("data/redundancy_zero.txt")
        compressed_code = coding(text)

        decode = decoding(compressed_code)

        self.assertEqual(text, decode, "The contents of the data are not the same!")

    def test_loremipsum_text(self):
        text = read_file("data/loremipsum.txt")
        compressed_code = coding(text)

        decode = decoding(compressed_code)

        self.assertEqual(text, decode, "The contents of the data are not the same!")


if __name__ == "__main__":
    unittest.main()
