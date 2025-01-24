# This function takes a word as a parameter and returns a dictionary that shows how many times each symbol appears in the word.
# The function is very simple but useful, as it is needed for both data compression algorithms.

def create_dict(word):
    dict = {}
    for i in word:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

