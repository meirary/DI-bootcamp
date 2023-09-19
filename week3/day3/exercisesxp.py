# Exercises 1

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.currency}"

    def __int__(self):
        return self.amount

    def __repr__(self):
        return f"{self.amount} {self.currency}"

    def __add__(self, other):
        if isinstance(other, Currency) and self.currency == other.currency:
            return Currency(self.currency, self.amount + other.amount)
        elif isinstance(other, (int, float)):
            return Currency(self.currency, self.amount + other)
        else:
            raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")

    def __iadd__(self, other):
        if isinstance(other, (int, float)):
            self.amount += other
        elif isinstance(other, Currency) and self.currency == other.currency:
            self.amount += other.amount
        else:
            raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
        return self

# Testing the Currency class
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))  # '5 dollars'
print(int(c1))  # 5
print(repr(c1))  # '5 dollars'
print(c1 + 5)  # 10 dollars
print(c1 + c2)  # 15 dollars
print(c1)  # 5 dollars

c1 += 5
print(c1)  # 10 dollars

c1 += c2
print(c1)  # 20 dollars

# This will raise a TypeError
try:
    c1 + c3
except TypeError as e:
    print(e)


# Exercises 3

import random
import string

def generate_random_string(length):
    characters = string.ascii_letters  # This includes both uppercase and lowercase letters

    random_string = ''.join(random.choice(characters) for _ in range(length))

    return random_string

random_string = generate_random_string(5)

print(random_string)

# Exercises 4

import datetime

def display_current_date():
    current_date = datetime.date.today()
    print("Current Date:", current_date)

display_current_date()

# Exercises 5

import datetime

def time_left_until_january_1st():
    current_datetime = datetime.datetime.now()

    next_year = current_datetime.year + 1
    target_date = datetime.datetime(next_year, 1, 1)

    time_difference = target_date - current_datetime

    days = time_difference.days
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    print(f"The 1st of January is in {days} days and {hours}:{minutes:02}:{seconds:02} hours.")

time_left_until_january_1st()

# Exercises 6

import datetime

def minutes_lived(birthdate):
    birthdate = datetime.datetime.strptime(birthdate, "%d-%m-%Y")

    current_datetime = datetime.datetime.now()

    time_difference = current_datetime - birthdate

    total_minutes_lived = time_difference.total_seconds() / 60

    return total_minutes_lived


birthdate = "19-09-1981"  # Replace with the user's birthdate in the specified format
minutes = minutes_lived(birthdate)
print(f"You have lived for approximately {minutes:.2f} minutes.")

# Exercises 7

from faker import Faker

users = []

fake = Faker()

def add_user():
    user = {
        'name': fake.name(),
        'address': fake.address(),
        'language_code': fake.language_code()
    }
    users.append(user)


for _ in range(10):  
    add_user()

for user in users:
    print(user)
