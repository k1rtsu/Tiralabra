import heapq  # The heapq module is used for implementing the priority queue, a critical part of the Huffman coding process.
import struct
from bitarray import bitarray


class Node:
    """
    Represents a node in the Huffman tree, containing frequency, symbol, and child nodes.
    """
    def __init__(self, freq=None, symbol=None):
        """
        Initializes a node with frequency, symbol, and optional child nodes.
        """
        self.freq = freq  # Frequency of the symbol
        self.symbol = symbol  # Symbol itself
        self.left = None  # Left child of the node
        self.right = None  # Right child of the node

    def __lt__(self, other):
        """
        Comparison method for ordering nodes by frequency and symbol length.
        """
        if self.freq != other.freq:
            return self.freq < other.freq
        return len(self.symbol) > len(other.symbol)

    def __str__(self):
        """
        String representation of the node.
        """
        return f"{self.symbol}::{self.freq}"


def create_dict(word):
    """
    Creates a frequency dictionary for each character in the input string 'word'.
    """
    freq_dict = {}
    for i in word:
        freq_dict[i] = freq_dict.get(i, 0) + 1
    return freq_dict


def create_queue(freq_dict):
    """
    Creates a priority queue (min-heap) from the frequency dictionary.
    """
    queue = []
    for symbol, freq in freq_dict.items():
        heapq.heappush(queue, Node(freq=freq, symbol=symbol))
    heapq.heapify(queue)
    return queue


def create_huffman_tree(queue):
    """
    Constructs the Huffman tree from the priority queue.
    Returns the root node of the Huffman tree.
    """
    while len(queue) > 1:
        node1 = heapq.heappop(queue)
        node2 = heapq.heappop(queue)
        new_node = Node(freq=node1.freq + node2.freq, symbol=node1.symbol + node2.symbol)
        new_node.left = node1
        new_node.right = node2
        heapq.heappush(queue, new_node)

    return queue[0] if queue else None


def coding(letter, node, code=""):
    """
    Recursively finds the Huffman code for a specific letter in the tree.
    """
    if node is None:
        return False

    if node.symbol == letter:
        return code

    if node.left and letter in node.left.symbol:
        return coding(letter, node.left, code + "0")

    if node.right and letter in node.right.symbol:
        return coding(letter, node.right, code + "1")

    return False


class HuffmanCode:
    """
    Manages the entire Huffman coding process, including tree construction and encoding.
    """
    def __init__(self, word):
        """
        Initializes the HuffmanCode instance by creating the frequency dictionary, queue, and Huffman tree.
        """
        self.word = word
        self.dict = create_dict(word)
        self.queue = create_queue(self.dict)
        self.huffman_tree = create_huffman_tree(self.queue)

    def tree(self):
        """
        Returns the root of the Huffman tree.
        """
        return self.huffman_tree

    def code(self):
        """
        Encodes the word into its Huffman binary representation.
        """
        return "".join(coding(i, self.huffman_tree) for i in self.word)


def decoding(code, tree: Node):
    """
    Decodes a binary string back into the original string using the Huffman tree.
    """
    decode = ""
    node = tree
    for bit in code:
        node = node.right if bit == "1" else node.left
        if len(node.symbol) == 1:
            decode += node.symbol
            node = tree
    return decode


def serialize_huffman_tree(node: Node):
    """
    Serializes the Huffman tree into a list of bits and symbols for file storage.
    """
    def traverse(node: Node, items):
        if not node:
            return
        if len(node.symbol) == 1:
            items.append(1)
            items.append(node.symbol)
        else:
            items.append(0)
        traverse(node.left, items)
        traverse(node.right, items)

    items = []
    traverse(node, items)
    return items


def deserialize_huffman_tree(items):
    """
    Deserializes a list of bits and symbols back into a Huffman tree.
    """
    def build(iterator):
        value = next(iterator)
        if value == 1:
            return Node(freq=0, symbol=next(iterator))
        node = Node(freq=0, symbol="")
        node.left = build(iterator)
        node.right = build(iterator)
        return node

    return build(iter(items))


def save_compressed_file(filename, huffman_tree, encoded_text):
    """
    Saves the serialized Huffman tree and encoded text into a compressed file.
    """
    tree_data = serialize_huffman_tree(huffman_tree)
    bitarr = bitarray(encoded_text)

    tree_data_bytes = bytearray()
    for item in tree_data:
        if item == 0:
            tree_data_bytes.append(0)
        else:
            tree_data_bytes.append(1)
            if isinstance(item, str):
                tree_data_bytes.extend(item.encode("utf-8"))

    with open(filename, "wb") as f:
        f.write(struct.pack("H", len(tree_data_bytes)))
        f.write(bytes(tree_data_bytes))
        f.write(struct.pack("I", len(bitarr)))
        bitarr.tofile(f)


def remove_one_of_consecutive_ones(data):
    """
    Removes redundant consecutive ones to clean up the serialized tree data.
    """
    result = []
    i = 0
    while i < len(data):
        if i < len(data) - 1 and data[i] == data[i + 1] == 1:
            result.append(1)
            i += 2
        else:
            result.append(data[i])
            i += 1
    return result


def load_compressed_file(filename):
    """
    Loads a compressed file, extracting the Huffman tree and encoded text.
    """
    with open(filename, "rb") as f:
        tree_length = struct.unpack("H", f.read(2))[0]
        tree_data_bytes = f.read(tree_length)

        tree_data = []
        i = 0
        while i < len(tree_data_bytes):
            if tree_data_bytes[i] == 0:
                tree_data.append(0)
                i += 1
            elif tree_data_bytes[i] == 1:
                tree_data.append(1)
                i += 1
                symbol_bytes = bytearray()
                while i < len(tree_data_bytes) and tree_data_bytes[i] not in [0, 1]:
                    symbol_bytes.append(tree_data_bytes[i])
                    i += 1
                if symbol_bytes:
                    tree_data.append(symbol_bytes.decode("utf-8"))

        tree_data = remove_one_of_consecutive_ones(tree_data)
        encoded_length = struct.unpack("I", f.read(4))[0] & ~(1 << 31)

        bitarr = bitarray()
        bitarr.fromfile(f)
        bitarr = bitarr[:encoded_length]

        huffman_tree = deserialize_huffman_tree(tree_data)
        return huffman_tree, bitarr.to01()
