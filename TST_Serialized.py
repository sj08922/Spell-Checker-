import pickle

def create_node(char):
    return {'char': char, 'left': None, 'mid': None, 'right': None, 'is_end_of_word': False}

def insert(node, word, index): #Average/worst Case: O(h) 
    if node == None:
        node = create_node(word[index])
    if word[index] < node['char']:
        node['left'] = insert(node['left'], word, index)
    elif word[index] > node['char']:
        node['right'] = insert(node['right'], word, index)
    elif index < len(word) - 1:
        node['mid'] = insert(node['mid'], word, index + 1)
    else:
        node['is_end_of_word'] = True
    return node
# Create an empty Ternary Search Tree
root = None

# Function to insert a word into the TST
def insert_word(word): #O(h), as it’s a wrapper for the insert function.
    global root
    root = insert(root, word, 0)

# Load dictionary words into TST
def construct_tst(): #Average/Worst Case: O(m * k), where m is the number of words in the dictionary and k is the average length of the words.
    with open("words_alpha.pkl", "r") as f:
        for line in f:
            insert_word(line.strip())

# serialize the TST to a file
def serialize(): # O(n) n is length of variable
    with open("Serialized_TST.pkl", 'wb') as file:
        pickle.dump(root, file)


construct_tst()
serialize()
