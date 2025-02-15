# The LZ78 algorithm is a data compression algorithm developed in 1978. 
# The algorithm compresses data by replacing repeated strings with shorter symbols. 
# It is also efficient because it does not require a separate dictionary; instead, it creates the dictionary while compressing the data.

def coding(w: str):
    if w == '':
        return []
    dictionary = {}
    compressed = []

    dict_index = 1
    char = ''
    for i in range(len(w)):
        if char + w[i] in dictionary:
            char += w[i]

        else:
            index = dictionary.get(char, 0)
            compressed.append((index, w[i]))
            dictionary[char + w[i]] = dict_index
            dict_index += 1
            char = ''


    if char:
        last_char = char[-1]
        other_char = char[:-1]
        index = dictionary.get(other_char, 0)
        compressed.append((index, last_char))

    return compressed


def decoding(code: list):
    if code == []:
        return ''
    dicttionary = {}
    decompressed = ''

    dict_index = 1
    for i in code:
        if i[0] == 0:
            dicttionary[dict_index] = i[1]
            decompressed += i[1]
            dict_index += 1

        else:
            decompressed += dicttionary[i[0]] + i[1]
            dicttionary[dict_index] = dicttionary[i[0]] + i[1]
            dict_index += 1

    return decompressed
