#Huffman coding is an algorithm developed in 1952 for data compression. HC is one of the older data compression algorithms, but it is still in use today. Huffman coding is based on the idea that frequently occurring characters are assigned shorter codes, while infrequent characters get longer codes.
#The algorithm is given a vocabulary that specifies how many times a particular symbol appears in the data. Based on this, the algorithm creates a binary tree, where the most frequent characters are closer to the root, and the less frequent characters are further away from the root.
import heapq  # The efficient heapq data structure is used to implement the Huffman tree.
from help import create_dict

class Node:  #Nodes are required to construct the Huffman tree. A Node object contains information about the symbol and its frequency.
    def __init__(self, freq=None, symbol=None):
        self.freq = freq
        self.symbol = symbol
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq
    
    def __str__(self):
        return f"{self.symbol}::{self.freq}"

def create_queue(dict):  #This function creates a priority queue that contains all characters and their frequencies.
    queue = []

    for i in dict:
        node = Node(freq=dict[i], symbol=i)
        heapq.heappush(queue, node)

    return queue

def create_huffman_tree(queue): #This function creates the Huffman tree based on the priority queue.
    while len(queue) > 1:
        node1 = heapq.heappop(queue)
        node2 = heapq.heappop(queue)

        new_node = Node(freq=node1.freq + node2.freq, symbol=node1.symbol + node2.symbol)
        new_node.left = node1
        new_node.right = node2

        heapq.heappush(queue, new_node)

    return queue

