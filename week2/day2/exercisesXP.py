# exercises 1
my_fav_numbers = {10, 20, 30, 40, 55}

my_fav_numbers.add(7)
my_fav_numbers.add(80)
print(my_fav_numbers)

my_fav_numbers.remove(30)
print(my_fav_numbers)

friend_fav_numbers = {12, 25, 42, 78}
print(friend_fav_numbers)


our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

# Exercises 2 
# its inmutable you cant do it.

# Exercises 3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana")
basket.remove("Blueberries")
print(basket)

basket.append("Kiwi")
basket.insert(0, "Apples")
print(basket)

apple_count = basket.count("Apples")
print(basket)

basket.clear()
print(basket)

# Exercises 4
# Float is a number with decimal, 
# # the difference between integer and float is that integer is the whole number and the floats number with fractional value.

sequence = []
start = 1.5
end = 5
step = 0.5

current_value = start
while current_value <= end:
    sequence.append(current_value)
    current_value += step

print(sequence)


# Exercises 5

print("All numbers from 1 to 20:")
for number in range(1, 21):
    print(number)

print("\nElements with even index:")
for number in range(1, 21):
    if number % 2 == 0:
        print(number)

# Exercises 6

your_name = "Meir"  

while True:
    user_name = input("Please enter your name: ")
    if user_name == your_name:
        print("Thank you for entering your name.")
        break
    else:
        print("Name does not match. Please try again.")


#Exercises 7

favorite_fruits_input = input("Enter your favorite fruit(s) separated by a space: ")

favorite_fruits = favorite_fruits_input.split()

user_input = input("Enter a fruit name: ")

if user_input in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy.")

# Exercises 8
toppings = []
total_price = 10  

while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    
    if topping.lower() == 'quit':
        break  
    
    toppings.append(topping)
    total_price += 2.5
    print(f"Adding {topping} to your pizza.")

if toppings:
    print("\nYour pizza toppings:")
    for topping in toppings:
        print("- " + topping)
    print(f"\nTotal price: ${total_price:.2f}")
else:
    print("\nNo toppings selected. Enjoy your plain pizza!")

# Exercises 9
total_cost = 0

num_people = int(input("Enter the number of people in the family: "))
for _ in range(num_people):
    age = int(input("Enter the age of a family member: "))
    
    if age < 3:
        ticket_cost = 0
    elif 3 <= age <= 12:
        ticket_cost = 10
    else:
        ticket_cost = 15
    
    total_cost += ticket_cost

print(f"The total cost of tickets for the family is ${total_cost}")

teenagers = ["Pedro", "Juan", "Ana", "David", "Sara"]

allowed_teens = []

for teen in teenagers:
    age = int(input(f"Enter the age of {teen}: "))
    if 16 <= age <= 21:
        allowed_teens.append(teen)

print("Teenagers allowed to watch the movie:")
print(allowed_teens)

# Exercises 10
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)  
    finished_sandwiches.append(current_sandwich)
    print(f"I made your {current_sandwich.lower()}")

print("\nSandwiches that were made:")
for sandwich in finished_sandwiches:
    print(sandwich)
