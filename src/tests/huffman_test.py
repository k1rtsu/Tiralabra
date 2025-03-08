import unittest
import sys
import os
sys.path.append(os.path.abspath("src"))
sys.path.append(os.path.abspath("data"))
sys.path.append(os.path.abspath("compressed"))
sys.path.append(os.path.abspath("decompressed"))

from algs.huffman import (
    create_dict,
    create_queue,
    create_huffman_tree,
    decoding,
    Node,
    HuffmanCode,
    serialize_huffman_tree,
    deserialize_huffman_tree,
    save_compressed_file,
    load_compressed_file,
)



def read_file(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        content = file.read()
    return content


class TestFunctions(unittest.TestCase):
    def test_create_dict(self):
        word = "abracadabra"
        answer = {"a": 5, "b": 2, "r": 2, "c": 1, "d": 1}
        test = create_dict(word)
        self.assertEqual(test, answer)

    def test_create_queue(self):
        word_dict = {"a": 5, "b": 2, "r": 2, "c": 1, "d": 1}
        queue = create_queue(word_dict)
        self.assertEqual(len(queue), 5)
        self.assertEqual(queue[0].symbol, "d")
        self.assertEqual(queue[0].freq, 1)

    def test_create_huffman_tree(self):
        word_dict = {"a": 5, "b": 2, "r": 2, "c": 1, "d": 1}
        queue = create_queue(word_dict)
        huffman_tree = create_huffman_tree(queue)
        self.assertIsInstance(huffman_tree, Node)
        self.assertEqual(huffman_tree.freq, 11)


class TestHuffmanCoding(unittest.TestCase):
    def test_coding(self):
        hc = HuffmanCode("abracadabra")
        answer = "01011101101011000101110"
        self.assertEqual(hc.code(), answer)

    def test_decoding(self):
        hc = HuffmanCode("abracadabra")
        code = hc.code()
        answer = "abracadabra"
        decode = decoding(code, hc.tree())
        self.assertEqual(decode, answer)

    def test_large_text(self):
        text = read_file("data/test_data/rc.txt")
        hc = HuffmanCode(text)
        compressed_code = hc.code()
        decode = decoding(compressed_code, hc.tree())
        self.assertEqual(text, decode, "The contents of the files are not the same!")

    def test_serialize_deserialize_tree(self):
        text = "abracadabra"
        hc = HuffmanCode(text)
        tree = hc.tree()
        serialized_tree = serialize_huffman_tree(tree)
        deserialized_tree = deserialize_huffman_tree(serialized_tree)
        self.assertEqual(decoding(hc.code(), deserialized_tree), text)

    def test_save_load_compressed_file(self):
        text = "abracadabra"
        hc = HuffmanCode(text)
        compressed_code = hc.code()
        tree = hc.tree()

        file_path = "data/compressed/test_compressed.txt"
        save_compressed_file(file_path, tree, compressed_code)
        loaded_tree, loaded_code = load_compressed_file(file_path)

        self.assertEqual(decoding(loaded_code, loaded_tree), text)
        os.remove(file_path)


if __name__ == "__main__":
    unittest.main()
