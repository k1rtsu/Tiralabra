#Huffman coding is an algorithm developed in 1952 for data compression. HC is one of the older data compression algorithms, but it is still in use today. Huffman coding is based on the idea that frequently occurring characters are assigned shorter codes, while infrequent characters get longer codes.
#The algorithm is given a vocabulary that specifies how many times a particular symbol appears in the data. Based on this, the algorithm creates a binary tree, where the most frequent characters are closer to the root, and the less frequent characters are further away from the root.
import heapq  # The efficient heapq data structure is used to implement the Huffman tree.

class Node:  #Nodes are required to construct the Huffman tree. A Node object contains information about the symbol and its frequency.
    def __init__(self, freq=None, symbol=None):
        self.freq = freq
        self.symbol = symbol
        self.left = None
        self.right = None

    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq
        

        return len(self.symbol) > len(other.symbol)
    
    def __str__(self):
        return f"{self.symbol}::{self.freq}"


def create_dict(word):
    dict = {}
    for i in word:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict


def create_queue(dict):  #This metod creates a priority queue that contains all characters and their frequencies.
    queue = []

    for i in dict:
        node = Node(freq=dict[i], symbol=i)
        heapq.heappush(queue, node)

    heapq.heapify(queue)

    return  queue


def create_huffman_tree(queue): #This metod creates the Huffman tree based on the priority queue.
    while len(queue) > 1:
        node1 = heapq.heappop(queue)
        node2 = heapq.heappop(queue)

        new_node = Node(freq=node1.freq + node2.freq, symbol=node1.symbol + node2.symbol)

        if len(new_node.symbol) == 3  and node1.freq == node2.freq:
            new_node.left = node2
            new_node.right = node1
        else:
            new_node.left = node1
            new_node.right = node2

        heapq.heappush(queue, new_node)
        heapq.heapify(queue)

    return queue[0]


def coding(letter, node, binString = ''):
    d = dict()
    if node.symbol == letter:
        return {letter: binString}

    if node.left.symbol == letter:
        d.update(coding(letter, node.left, binString + '0'))
        return d
    
    d.update(coding(letter, node.right, binString + '1'))
    return d




class HuffmanCode:  #The HuffmanCode class contains the Huffman coding algorithm. The class is initialized with a word, and the algorithm creates a dictionary of the word's characters and their frequencies.
    def __init__(self, word):
        self.word = word
        self.dict = create_dict(word)
        self.queue = create_queue(self.dict)
        self.huffman_tree = create_huffman_tree(self.queue)

    def alphabet(self):
        alphabet = {}

        for i in self.word:
            if i in alphabet:
                continue

            alphabet[i] = coding(i, self.huffman_tree)[i]

        return alphabet

    def tree(self):
        return self.huffman_tree
    
    def q(self):
        return self.queue()
    
    def d(self):
        return self.dict()
    
    def coding(self):
        code = []

        alphabet = self.alphabet()

        for i in self.word:
            code.append(alphabet[i])

        return code

class HuffmanDeCode:
    def __init__(self, code:list, alphabet:dict):
        self.code = code
        self.alphabet = {v: k for k, v in alphabet.items()}

    def decoding(self):
        decode = ''

        for i in self.code:
            decode += self.alphabet[i]

        return decode
