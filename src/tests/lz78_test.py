import unittest
import sys
import os
import ast

sys.path.append(os.path.abspath("src"))

from algs.lz78 import coding, decoding

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()

    return content

def write_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(data)

def read_list_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read().strip()
        return ast.literal_eval(data)


class TestLZ78(unittest.TestCase):
    def test_coding(self):
        word = 'abracadabra'
        code = coding(word)
        answer = [(0, 'a'), (0, 'b'), (0, 'r'), (1, 'c'), (1, 'd'), (1, 'b'), (3, 'a')]

        self.assertEqual(answer, code)


    def test_decoding(self):
        word = 'abracadabra'
        code = coding(word)
        decode = decoding(code)

        self.assertEqual(decode, word)

    def test_large_text(self):
        text = read_file('data/rc.txt')
        write_file('compressed/coded_rc_lz.txt', str(coding(text)))

        code = read_list_from_file('compressed/coded_rc_lz.txt')
        write_file('decompressed/dc_rc_lz.txt', decoding(code))

        file_out = read_file('decompressed/dc_rc_lz.txt')

        self.assertEqual(text, file_out, "The contents of the files are not the same!")

    def test_empty_text(self):
        text = read_file('data/empty.txt')
        write_file('compressed/coded_empty_lz.txt', str(coding(text)))

        code = read_list_from_file('compressed/coded_empty_lz.txt')
        write_file('decompressed/dc_empty_lz.txt', decoding(code))

        file_out = read_file('decompressed/dc_empty_lz.txt')

        self.assertEqual(text, file_out)

    def test_zeroredundancy_text(self):
        text = read_file('data/redundancy_zero.txt')
        write_file('compressed/coded_redundancy_zero.txt', str(coding(text)))

        code = read_list_from_file('compressed/coded_redundancy_zero.txt')
        write_file('decompressed/dc_redundancy_zero.txt', decoding(code))

        file_out = read_file('decompressed/dc_redundancy_zero.txt')

        self.assertEqual(text, file_out)

if __name__ == '__main__':
    unittest.main()
