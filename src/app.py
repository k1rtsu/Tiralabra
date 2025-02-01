import sys
import os

# Lisää 'src' hakupolkuun
sys.path.append(os.path.abspath("src"))

from algs.huffman import HuffmanCode, HuffmanDeCode

word = HuffmanCode("abracadabra")

code = word.coding()
alphabet = word.alphabet()

print(code) 
print(alphabet)

print('///////////////')

koodi = HuffmanDeCode(code, alphabet)
dekodi = koodi.decoding()
print(dekodi)

def tree_out(tree, level=0):
    if tree is not None:
        print("   " * level + f"{tree.symbol}::{tree.freq}")  
        tree_out(tree.left, level + 1)
        tree_out(tree.right, level + 1)

tree = word.tree()
tree_out(tree)