# Exercises 1
number = int(input("Enter a number: "))

length = int(input("Enter the desired length: "))

multiples_list = []

for i in range(1, length + 1):
    multiple = number * i
    multiples_list.append(multiple)

print(multiples_list)

# Exercises 2
user_string = input("Enter a string: ")

result_string = ""

prev_char = ""

for char in user_string:
    if char != prev_char:
        result_string += char  
    prev_char = char  

print(result_string)

