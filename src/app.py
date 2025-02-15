import sys
import os
import ast

sys.path.append(os.path.abspath('src'))
sys.path.append(os.path.abspath('data'))
sys.path.append(os.path.abspath('compressed'))
sys.path.append(os.path.abspath('decompressed'))

from algs.huffman import HuffmanCode, decoding
import algs.lz78 

def tree_out(tree, level=0):
    if tree is not None:
        print("   " * level + f"{tree.symbol}::{tree.freq}")
        tree_out(tree.left, level + 1)
        tree_out(tree.right, level + 1)

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()

    return content

def write_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(data)

def read_list_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read().strip()
        return ast.literal_eval(data)


algoritm = input('which algorithm you want to try: a - Huffmancoding, b - Lz78: ')
type_of_input = input('do you want to compress phrase/word or file? f-file w-word: ')

if type_of_input == 'w':
    word = input('Put word or phrase there:')

    if algoritm == 'a':
        hc = HuffmanCode(word)
        code = hc.code()
        print('Huffmans tree used in compression')
        tree_out(hc.tree())
        print(f'Coded output {code}')

    if algoritm == 'b':
        lz = algs.lz78.coding(word)
        print(f'Output code: {lz}')

    dc = input('press y if u want to decode your code: )')

    if dc == 'y' and algoritm == 'a':
        print(f'Decode: {decoding(code, hc.tree())}')

    if dc == 'y' and algoritm == 'b':
        print(f'Decode: {algs.lz78.decoding(lz)}')

if type_of_input == 'f':
    print([file for file in os.listdir('data') if file.endswith('.txt')])
    file = input('chose one of the files you want to compress and write it there: ')

    if algoritm == 'a':
        hc = HuffmanCode(read_file(f'data/{file}'))
        code = hc.code()
        tree = hc.tree()
        tree_input = input('Do you want to see huffmans tree of this code: y-yes n-not  ')
        if tree_input == 'y':
            print('Huffmans tree used in compression')
            tree_out(hc.tree())

        write_file(f'compressed/coded_{file}', str(code))
    
    if algoritm == 'b':
        lz = algs.lz78.coding(read_file(f'data/{file}'))
        write_file(f'compressed/coded_{file}', str(lz))
        
    print('You can find your code in compressed folde')


    dc = input('press y if u want to decode your code: )')
    code = read_list_from_file(f'compressed/coded_{file}')

    if dc == 'y' and algoritm == 'a':
        write_file(f'decompressed/dc{file}', decoding(code, tree))

    if dc == 'y' and algoritm == 'b':
        write_file(f'decompressed/dc{file}', algs.lz78.decoding(code))

    print('Now u can find decoded file in decompessed folder')
