import string
from collections import Counter

class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word):
        words = self.text.split()
        word_count = words.count(word)
        return f"'{word}' appears {word_count} times in the text."

    def most_common_word(self):
        words = self.text.split()
        word_counts = Counter(words)
        most_common = word_counts.most_common(1)
        return f"The most common word in the text is '{most_common[0][0]}'."

    def unique_words(self):
        words = self.text.split()
        unique_words = set(words)
        return list(unique_words)

# Example:
text = "This is a story about two sisters, Elsa, and Anna who have eternal bonds and love for each other. Elsa appears to be calm, reserved, and regal. She is quite turbulent because of her strong magical powers. On the other hand, Anna is optimistic, energetic, elegant, and free-spirited. She is over-friendly and trusts strangers very quickly.This story conveys a lot."
text_analyzer = Text(text)

print(text_analyzer.word_frequency("and"))
print(text_analyzer.most_common_word())
print(text_analyzer.unique_words())


# Part 2

class Text:
    def __init__(self, text):
        self.text = text

    @classmethod
    def from_file(cls, filename):
        try:
            with open(filename, 'r') as file:
                file_text = file.read()
            return cls(file_text)
        except FileNotFoundError:
            print("File not found.")
            return None


text_from_file = Text.from_file('text.txt')
if text_from_file:
    print(text_from_file.text)
