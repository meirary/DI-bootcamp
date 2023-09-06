# Exercises 1
list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1.extend(list2)
print(list1)

# Exercises 2
for num in range(1500, 2501):
    if num % 5 == 0 and num % 7 == 0:
        print(num)

# Exercises 3
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

user_name = input("Enter your name: ")

if user_name in names:
    index = names.index(user_name)
    print(f"The index of the first occurrence of {user_name} is {index}")
else:
    print(f"{user_name} is not in the list.")

# Exercises 4

num1 = float(input("Input the 1st number: "))
num2 = float(input("Input the 2nd number: "))
num3 = float(input("Input the 3rd number: "))

greatest_number = max(num1, num2, num3)

print(f"The greatest number is: {greatest_number}")

# Exercises 5
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for letter in alphabet:
    if letter in 'aeiou':
        print(f'{letter} is a vowel.')
    else:
        print(f'{letter} is a consonant.')

# Exercises 6
words = []
for _ in range(7):
    word = input("Enter a word: ")
    words.append(word)

letter = input("Enter a single character: ")

for word in words:
    if letter in word:
        index = word.index(letter)
        print(f"The index of '{letter}' in '{word}' is {index}.")
    else:
        print(f"'{letter}' is not found in '{word}'.")

# Exercises 7
numbers = list(range(1, 1000001))

minimum = min(numbers)
maximum = max(numbers)

total_sum = sum(numbers)

print(f"Minimum value: {minimum}")
print(f"Maximum value: {maximum}")
print(f"Sum of all numbers: {total_sum}")

# Exercises 8
input_sequence = input("Enter a sequence of comma-separated numbers: ")

numbers_list = input_sequence.split(',')

numbers_tuple = tuple(numbers_list)

print(numbers_list)
print(numbers_tuple)

