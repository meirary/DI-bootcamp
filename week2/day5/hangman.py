import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist)

# Convert the chosen word to uppercase for case-insensitive comparisons
word = word.upper()

def display_word(word, guessed_letters):
    """Display the word with asterisks for hidden letters."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "*"
    return display

def hangman():
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("You have 6 attempts to guess the word.")

    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        guess = input("Guess a letter: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!")
        else:
            print("Incorrect guess.")
            attempts -= 1

        if set(guessed_letters) == set(word):
            print("\nCongratulations! You've guessed the word:", word)
            break

    if attempts == 0:
        print("\nYou've run out of attempts. The word was:", word)

if __name__ == "__main__":
    hangman()
