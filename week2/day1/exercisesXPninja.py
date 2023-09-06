# exercises 3
# >>> 3 <= 3 < 9
#     >>> 3 == 3 == 3
#     >>> bool(0)
#     >>> bool(5 == "5")
#     >>> bool(4 == 4) == bool("4" == "4")
#     >>> bool(bool(None))
#     x = (1 == True)
#     y = (1 == False)
#     a = True + 4
#     b = False + 10

#     print("x is", x)
#     print("y is", y)
#     print("a:", a)
#     print("b:", b)

# Exercises 4

# my_text = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit essecillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

# char_count = len(my_text)

# print (char_count)  


# Exercises 5
longest_sentence = ""

while True:
    sentence = input("Enter the longest sentence without the letter 'A' (or type 'quit' to exit): ")

    if sentence.lower() == "quit":
        break  

    if 'A' not in sentence and len(sentence) > len(longest_sentence):
        longest_sentence = sentence
        print("Congratulations! You've set a new longest sentence.")

print(f"The longest sentence without the letter 'A' is: {longest_sentence}")