# Exercise
#  1. create a function that takes a number as an argument, and check if this number is even or odd
# 2. create a function that takes a list of numbers as an argument, and check if each number is even or odd

def check(num):
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")

check(5)
check(18)
check(45)

# Exercises 2



def check_all_numbers(list_numbers):
    for num in list_numbers:
        if num % 2 == 0:
            print(f"{num} is even.")
        else:
            print(f"{num} is odd.")


check_all_numbers ([30,45,67,88,90,102])

# Exercises 3
# 1st function - get_price_car
# receive the age of the user 
# and if the user is > 40
#     --> 200
# if the user is < 40
#     --> 300

def get_price_car(age):
    if age > 40:
        return 200
    else:
        return 300  

user_age = 20  
price = get_price_car(user_age)
print(f"The car price for a {user_age}-year-old user is ${price}")




def get_price_flight(destination):
    if destination == "Paris":
        return 400
    else:
        return 600

user_destination = "Paris" 
price = get_price_flight(user_destination)
print(f"The Flight price for a {user_destination}- is ${price}")

# 2nd function - get_price_flight
# receive a destination from the user
# if the destinatation is Paris
#     --> 400
# if the destinatation is Paris
#     --> 600

# 3rd function
# is going to use the result from the 2 functions above
# and inform the user of the total price of the vacation

def find_sum():
    price_car= get_price_car(user_age)
    fight_price = get_price_flight (user_destination)
    
    total =  price_car + fight_price
    print(f"your vacation will cost {total} dollars ")

find_sum()











