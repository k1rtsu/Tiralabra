import sys
import os
import ast
from time import time

sys.path.append(os.path.abspath('src'))
sys.path.append(os.path.abspath('data'))
sys.path.append(os.path.abspath('compressed'))
sys.path.append(os.path.abspath('decompressed'))

from algs.huffman import HuffmanCode, decoding
import algs.lz78 

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

#LOREMIPSUM
print('Testing with Loremipsum 1MB text')

loremipsum = read_file('data/loremipsum.txt')

print('Huffman coding:')
start_time = time()
hc = HuffmanCode(loremipsum)
hc_code = hc.code()
hc_dc = decoding(hc_code, hc.tree())
end_time = time()
print(True if hc_dc == loremipsum else False)
print(f'Time HC: {end_time - start_time}')

print('Lz-78:')
start_time = time()
lz_code = algs.lz78.coding(loremipsum)
lz_dc = algs.lz78.decoding(lz_code)
end_time = time()
print(True if lz_dc == loremipsum else False)
print(f'Time LZ-78: {end_time - start_time}')

#ROBINZON CRUZO
print()
print('Testing with Robinzon Cruzo chapters 1-5:')

rc = read_file('data/rc.txt')

start_time = time()
hc = HuffmanCode(rc)
hc_code = hc.code()
hc_dc = decoding(hc_code, hc.tree())
end_time = time()
print(True if hc_dc == rc else False)
print(f'Time HC: {end_time - start_time}')

print('Lz-78:')
start_time = time()
lz_code = algs.lz78.coding(rc)
lz_dc = algs.lz78.decoding(lz_code)
end_time = time()
print(True if lz_dc == rc else False)
print(f'Time LZ-78: {end_time - start_time}')

