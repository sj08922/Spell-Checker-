import pickle
import re

# Function to deserialize the TST from a file
def deserialize_tst(): #O(n)
    with open("Serialized_TST.pkl", 'rb') as file:
        return pickle.load(file)
root = deserialize_tst()

def search(node, word, index): #Average/worst Case: O(h)
    if node == None  or index >= len(word):
        return False
    if word[index] < node['char']:
        return search(node['left'], word, index)
    elif word[index] > node['char']:
        return search(node['right'], word, index)
    elif index < len(word) - 1:
        return search(node['mid'], word, index + 1)
    else:
        return node['is_end_of_word']
    
# Function to check spelling
def check_spelling(sentence): #Average/worst Case: O(n * k), where n is the number of words in the sentence and k is the average length of the words. Each word is checked using the search function
    words = re.split(r'[ ,.]+', sentence.lower())  # Convert sentence to lowercase and split into words
    misspelled_words = []
    for word in words:
        if search(root, word, 0) == False:
            misspelled_words.append(word)
    return words, misspelled_words
    
