# Exercises 1
print("Hello world\n" * 4, end="")

# Exercises 2
somemath = (99 ** 3) * 8
print(somemath)

# Exercises 3
# # Output: False
# print(5 < 3)  

# # Output: True
# print(3 == 3)  

# # Output: False
# print(3 == "3")  

# # Compare "3" (string) to 3 (integer) using ">", this will raise a TypeError

# print("3" > 3)

# # Output: False
# print("Hello" == "hello")  

# Exercises 4
computer_brand = "Dell"  
print(f"I have a {computer_brand} computer")

# Exercises 5
name = "Meir"  
age = 42  
shoe_size = 11  

info = f"My name is {name}. I am {age} years old, and my shoe size is {shoe_size}."

print(info)

# Exercises 6
a = 10
b = 8

if a > b:
    print("Hello World")

# Exercises 7
user_input = input("Enter a number: ")
number = int(user_input)

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

# Exercises 8
user_name = input("What's your name? ")

my_name = "Meir"

if user_name.lower() == my_name.lower():
    print("Hey, we have the same name!")
else:
    print(f"Hi {user_name}! I'm {my_name}. We don't have the same name, but you can change it!")

# Exercises 9
height_inches = float(input("Please enter your height in inches: "))

height_cm = height_inches * 2.54

ride_height_threshold = 145

if height_cm >= ride_height_threshold:
    print("You are tall enough to ride!")
else:
    print("Sorry, you need to grow some more to ride.")


