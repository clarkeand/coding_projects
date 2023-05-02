"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    whatev_works = open(file_path)
    whole_file = whatev_works.read().split()
    return whole_file




def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    tuple_list = []

    for idx in range(len(text_string)-1):
        key_tuple = ()
        new_value = idx + 1
        key_tuple = (text_string[idx], text_string[new_value])
        tuple_list.append(key_tuple)
    
    for tup in tuple_list:
        for idx, word in text_string:
            x = idx + 1
            if tup[1] == word:
                chains[tup] = [text_string[x]]


        

    # for idx, word in text_string:
    #     key_tuple = ()
    #     new_value = idx + 1
    #     key_tuple.add(word[idx], word[new_value])
    #     tuple_list.append(key_tuple)
        
    print(chains)
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
