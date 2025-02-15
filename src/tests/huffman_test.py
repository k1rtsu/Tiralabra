import unittest
import sys
import os
import heapq
import ast

sys.path.append(os.path.abspath("src"))
sys.path.append(os.path.abspath("data"))
sys.path.append(os.path.abspath("compressed"))
sys.path.append(os.path.abspath("decompressed"))

from algs.huffman import create_dict, create_queue, create_huffman_tree, coding, decoding, Node, HuffmanCode

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

class TestFunctions(unittest.TestCase):
    def test_create_dict(self):
        word = 'abracadabra'
        answer = {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
        test = create_dict(word)
        self.assertEqual(test, answer)

    def test_create_queue(self):
        word_dict = {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
        queue = create_queue(word_dict)
        self.assertEqual(len(queue), 5)
        self.assertEqual(queue[0].symbol, 'd')
        self.assertEqual(queue[0].freq, 1)

    def test_create_huffman_tree(self):
        word_dict = {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
        queue = create_queue(word_dict)
        huffman_tree = create_huffman_tree(queue)

        self.assertIsInstance(huffman_tree, Node)
        self.assertEqual(huffman_tree.freq, 11)

class TestHuffmanCoding(unittest.TestCase):
    def test_coding(self):
        hc = HuffmanCode('abracadabra')
        answer = ['0', '10', '111', '0', '1101', '0', '1100', '0', '10', '111', '0']

        self.assertEqual(hc.code(), answer)

    def test_decoding(self):
        hc = HuffmanCode('abracadabra')
        code = hc.code()
        answer = 'abracadabra'
        decode = decoding(code, hc.tree())

        self.assertEqual(decode, answer)

    def test_large_text(self):
        text = read_file('data/rc.txt')
        hc = HuffmanCode(text)
        write_file('compressed/coded_rc.txt', str(hc.code()))

        code = read_list_from_file('compressed/coded_rc.txt')
        write_file('decompressed/dc_rc.txt', decoding(code, hc.tree()))

        file_in = read_file('data/rc.txt')
        file_out = read_file('decompressed/dc_rc.txt')

        self.assertEqual(file_in, file_out, "The contents of the files are not the same!")

    def test_empty_text(self):
        text = read_file('data/empty.txt')
        hc = HuffmanCode(text)
        write_file('compressed/coded_empty.txt', str(hc.code()))

        code = read_list_from_file('compressed/coded_empty.txt')
        write_file('decompressed/dc_empty.txt', decoding(code, hc.tree()))

        file_in = read_file('data/empty.txt')
        file_out = read_file('decompressed/dc_empty.txt')

        self.assertEqual(file_in, file_out, "The contents of the files are not the same!")

    
    def test_zeroredundancy_text(self):
        text = read_file('data/redundancy_zero.txt')
        hc = HuffmanCode(text)
        write_file('compressed/coded_redundancy_zero.txt', str(hc.code()))

        code = read_list_from_file('compressed/coded_redundancy_zero.txt')
        write_file('decompressed/dc_redundancy_zero.txt', decoding(code, hc.tree()))

        file_in = read_file('data/redundancy_zero.txt')
        file_out = read_file('decompressed/dc_redundancy_zero.txt')

        self.assertEqual(file_in, file_out, "The contents of the files are not the same!")


if __name__ == '__main__':
    unittest.main()
