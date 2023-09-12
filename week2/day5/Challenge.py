# Exercises 1

input_sequence = input("Enter a comma-separated sequence of words: ")

words = [word.strip() for word in input_sequence.split(',')]


sorted_words = sorted(words)

result = ','.join(sorted_words)

print("Sorted sequence:", result)


# Exercises 2

import string

def longest_word(sentence):
    words = sentence.translate(str.maketrans('', '', string.punctuation)).split()

    if not words:
        return None  

    longest = words[0]  

    
    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


print(longest_word("Margaret's toy is a pretty doll."))  
print(longest_word("A thing of beauty is a joy forever.")) 
print(longest_word("Forgetfulness is by all means powerless!")) 
