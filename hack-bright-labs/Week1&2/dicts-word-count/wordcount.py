"""Count words in file."""

the_file = open("test.txt")
word_count_dictionary = {}

for row in the_file: 
    line = row.rstrip()
    words = line.split(' ')

    for word in words:
        
        word = word.lower()

        if word[len(word)-1] in ['.',',','!','?']:
            word = word[:len(word)-1:]

        if word not in word_count_dictionary: 
            word_count_dictionary[word] = 1

        else: 
            word_count_dictionary[word] += 1

for words, number in word_count_dictionary.items():
     print(f'{words} {number}')
