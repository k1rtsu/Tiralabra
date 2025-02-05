import sys
import os

# Lisää 'src' hakupolkuun
sys.path.append(os.path.abspath("src"))

from algs.huffman import HuffmanCode, decoding

def tree_out(tree, level=0):
    if tree is not None:
        print("   " * level + f"{tree.symbol}::{tree.freq}")  # Tulostetaan solmu sisennyksellä
        tree_out(tree.left, level + 1)  # Käydään vasen haara läpi
        tree_out(tree.right, level + 1)  # Käydään oikea haara läpi

s = 'Huffaminen algoritmi toimii!!!'

sana = HuffmanCode(s)

tree = sana.tree()

koodi = sana.code()

dekodi = decoding(koodi, tree)

print(s)
print('////////////////////')
print(koodi)
print('////////////////////')
tree_out(tree)
print('////////////////////')
print(dekodi)