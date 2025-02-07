import sys
import os

sys.path.append(os.path.abspath("src"))

from algs.huffman import HuffmanCode, decoding
import algs.lz78 

def tree_out(tree, level=0):
    if tree is not None:
        print("   " * level + f"{tree.symbol}::{tree.freq}")
        tree_out(tree.left, level + 1)
        tree_out(tree.right, level + 1)


algoritm = input('which algorithm you want to try: a - Huffmancoding, b - Lz78 ')
word = input('insert a word or phrase: ')

if algoritm == 'a':
    hc = HuffmanCode(word)
    code = hc.code()
    print('Huffmans tree used in compression')
    tree_out(hc.tree())
    print(f'Coded output {code}')

if algoritm == 'b':
    lz = algs.lz78.coding(word)
    print(f'Output code: {lz}')

dc = input('press y if u want to decode your code :)')

if dc == 'y' and algoritm == 'a':
    print(f'Decode: {decoding(code, hc.tree())}')

if dc == 'y' and algoritm == 'b':
    print(f'Decode: {algs.lz78.decoding(lz)}')
