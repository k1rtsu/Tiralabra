import unittest
import sys
import os
import heapq

sys.path.append(os.path.abspath("src"))

from algs.lz78 import coding, decoding


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

