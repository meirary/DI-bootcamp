
user_input = input("Enter a string with exactly 10 characters: ")

if len(user_input) < 10:
    print("String not long enough.")
elif len(user_input) > 10:
    print("String too long.")
else:
    print("Perfect string")

    print(f"First character: {user_input[0]}")
    print(f"Last character: {user_input[-1]}")


    for i in range(1, len(user_input) + 1):
        print(user_input[:i])

    import random

    char_list = list(user_input)
    random.shuffle(char_list)

    shuffled_string = ''.join(char_list)
    print(f"Jumbled string: {shuffled_string}")
