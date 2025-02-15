import sys
import os
import ast

sys.path.append(os.path.abspath("src"))

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
    
kansio = "data"  # Muuta tämä halutun kansion nimeksi

# Listataan kaikki .txt-tiedostot kansiossa
tiedostot = [tiedosto for tiedosto in os.listdir(kansio) if tiedosto.endswith(".txt")]

# Tulostetaan tiedostojen nimet
for tiedosto in tiedostot:
    print(tiedosto)