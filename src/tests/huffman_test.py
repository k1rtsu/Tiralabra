import unittest
import sys
import os
import heapq

sys.path.append(os.path.abspath("src"))

from algs.huffman import create_dict, create_queue, create_huffman_tree, coding, decoding, Node, HuffmanCode

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
        object = HuffmanCode('abracadabra')
        answer = ['0', '10', '111', '0', '1101', '0', '1100', '0', '10', '111', '0']

        self.assertEqual(object.code(), answer)

    def test_decoding(self):
        object = HuffmanCode('abracadabra')
        code = object.code()
        answer = 'abracadabra'
        decode = decoding(code, object.tree())

        self.assertEqual(decode, answer)


if __name__ == '__main__':
    unittest.main()
