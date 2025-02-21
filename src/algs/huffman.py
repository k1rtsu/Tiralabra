import heapq  # The heapq module is used for implementing the priority queue, a critical part of the Huffman coding process.
import struct
from bitarray import bitarray


class Node:  # Represents a node in the Huffman tree, which contains the frequency, symbol, and references to left and right children.
    def __init__(self, freq=None, symbol=None):
        self.freq = freq  # Frequency of the symbol
        self.symbol = symbol  # Symbol itself
        self.left = None  # Left child of the node
        self.right = None  # Right child of the node

    def __lt__(self, other):
        # Comparison method to ensure nodes are ordered by frequency, and in case of ties, by the length of the symbol.
        if self.freq != other.freq:
            return self.freq < other.freq
        return len(self.symbol) > len(other.symbol)

    def __str__(self):
        return f"{self.symbol}::{self.freq}"  # String representation for easier visualization of nodes


def create_dict(word):
    """
    Creates a dictionary with the frequency of each character in the input string 'word'.
    """
    dict = {}
    for i in word:
        if i in dict:
            dict[
                i
            ] += 1  # Increment the count for the character if it already exists in the dictionary
        else:
            dict[i] = 1  # Initialize the count for a new character
    return dict


def create_queue(dict):
    """
    Creates a priority queue (min-heap) from the dictionary, with nodes sorted by frequency.
    Each node in the queue represents a character and its frequency.
    """
    queue = []
    for i in dict:
        node = Node(freq=dict[i], symbol=i)
        heapq.heappush(queue, node)  # Add nodes to the heapq priority queue

    heapq.heapify(queue)  # Ensure the heap property is maintained
    return queue


def create_huffman_tree(queue):
    """
    Constructs the Huffman tree by repeatedly merging the two nodes with the lowest frequencies.
    Returns the root node of the Huffman tree.
    """
    while len(queue) > 1:
        node1 = heapq.heappop(queue)  # Remove the node with the smallest frequency
        node2 = heapq.heappop(queue)  # Remove the next node with the smallest frequency

        new_node = Node(
            freq=node1.freq + node2.freq, symbol=node1.symbol + node2.symbol
        )
        new_node.left = node1  # The left child of the new node is the first node
        new_node.right = node2  # The right child of the new node is the second node

        heapq.heappush(queue, new_node)  # Add the new node back to the queue

    if len(queue) > 0:
        return queue[0]  # Return the root node if the tree is built
    else:
        return queue  # Return the queue if no nodes remain


def coding(letter, node, code=""):
    """
    Recursively traverses the Huffman tree to find the Huffman code for a specific letter.
    Returns the binary code for the letter.
    """
    if node is None:
        return False

    if node.symbol == letter:
        return code  # Return the binary code when the letter is found

    if node.left and letter in node.left.symbol:
        result = coding(
            letter, node.left, code + "0"
        )  # Traverse left with '0' added to the code
        if result:
            return result

    if node.right and letter in node.right.symbol:
        result = coding(
            letter, node.right, code + "1"
        )  # Traverse right with '1' added to the code
        if result:
            return result

    return False  # Return False if the letter is not found


class HuffmanCode:
    """
    The HuffmanCode class manages the entire Huffman coding process, including tree construction and encoding.
    It is initialized with a word, and builds the corresponding Huffman tree.
    """

    def __init__(self, word):
        self.word = word  # The word to be compressed
        self.dict = create_dict(word)  # Create a frequency dictionary for the word
        self.queue = create_queue(
            self.dict
        )  # Create a priority queue from the frequency dictionary
        self.huffman_tree = create_huffman_tree(
            self.queue
        )  # Construct the Huffman tree

    def tree(self):
        return self.huffman_tree  # Returns the root of the Huffman tree

    def code(self):
        result = ""
        for i in self.word:
            result += coding(
                i, self.huffman_tree
            )  # Append the Huffman code for each letter
        return result  # Return the complete encoded string


def decoding(code, tree: Node):
    """
    Decodes a binary string using the Huffman tree and returns the original string.
    """
    decode = ""
    node = tree  # Start at the root of the Huffman tree
    for i in code:
        if i == "1":
            node = node.right  # Move to the right child for '1'
        if i == "0":
            node = node.left  # Move to the left child for '0'

        if len(node.symbol) == 1:  # If a leaf node is reached
            decode += node.symbol  # Add the symbol to the decoded string
            node = tree  # Reset to the root for the next character

    return decode  # Return the fully decoded string


def serialize_huffman_tree(node: Node):
    """
    Serializes the Huffman tree into a list of bits and symbols to be saved to a file.
    This process converts the tree structure into a format suitable for storage.
    """

    def traverse(node: Node, items):
        if not node:
            return
        if len(node.symbol) == 1:
            items.append(1)  # Leaf node, append 1 and the symbol
            items.append(node.symbol)
        else:
            items.append(0)  # Internal node, append 0
        traverse(node.left, items)  # Recursively traverse left child
        traverse(node.right, items)  # Recursively traverse right child

    items = []
    traverse(node, items)  # Start the traversal from the root node
    return items  # Return the serialized representation of the tree


def deserialize_huffman_tree(items):
    """
    Deserializes a list of bits and symbols back into a Huffman tree structure.
    This process reconstructs the Huffman tree from its serialized representation.
    """

    def build(iterator):
        value = next(iterator)
        if value == 1:  # If the value is 1, it's a leaf node
            symbol = next(iterator)
            return Node(freq=0, symbol=symbol)

        node = Node(freq=0, symbol="")  # Internal node
        node.left = build(iterator)  # Build the left child
        node.right = build(iterator)  # Build the right child
        return node

    return build(iter(items))  # Rebuild the tree from the list


def save_compressed_file(filename, huffman_tree, encoded_text):
    """
    Saves the Huffman tree and encoded text to a compressed file.
    The tree is serialized, and the encoded text is written as a bitarray.
    """
    tree_data = serialize_huffman_tree(huffman_tree)  # Serialize the Huffman tree
    bitarr = bitarray(encoded_text)  # Convert the encoded text into a bitarray

    tree_data_bytes = bytearray()
    for item in tree_data:
        if item == 0:
            tree_data_bytes.append(0)  # Append 0 for internal nodes
        else:
            tree_data_bytes.append(1)  # Append 1 for leaf nodes
            if isinstance(item, str):
                tree_data_bytes.extend(item.encode("utf-8"))  # Encode the symbol

    with open(filename, "wb") as f:
        f.write(
            struct.pack("H", len(tree_data_bytes))
        )  # Write the length of the tree data
        f.write(bytes(tree_data_bytes))  # Write the tree data
        f.write(struct.pack("I", len(bitarr)))  # Write the length of the encoded text
        bitarr.tofile(f)  # Write the bitarray of the encoded text


def remove_one_of_consecutive_ones(data):
    """
    Removes redundant consecutive ones from the tree data to ensure that the deserialized Huffman tree
    is identical to the original tree.
    """
    result = []
    i = 0
    while i < len(data):
        if i < len(data) - 1 and data[i] == data[i + 1] == 1:
            result.append(1)  # Keep one of the consecutive ones
            i += 2  # Skip the next consecutive one
        else:
            result.append(data[i])  # Append the current bit
            i += 1
    return result


def load_compressed_file(filename):
    """
    Loads a compressed file, extracting the Huffman tree and the encoded text.
    The tree is deserialized, and the encoded text is converted back from a bitarray.
    """
    with open(filename, "rb") as f:
        tree_length = struct.unpack("H", f.read(2))[
            0
        ]  # Read the length of the tree data
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

        tree_data = remove_one_of_consecutive_ones(tree_data)  # Clean up the tree data
        encoded_length = struct.unpack("I", f.read(4))[0] & ~(
            1 << 31
        )  # Read the length of the encoded data

        bitarr = bitarray()
        bitarr.fromfile(f)
        bitarr = bitarr[:encoded_length]  # Trim the bitarray to the correct length

        huffman_tree = deserialize_huffman_tree(
            tree_data
        )  # Reconstruct the Huffman tree
        return (
            huffman_tree,
            bitarr.to01(),
        )  # Return the Huffman tree and the encoded string
