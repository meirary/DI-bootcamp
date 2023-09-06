# Exercises 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result_dict = dict(zip(keys, values))

print(result_dict)

# Exercises 2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

total_cost = 0

for name, age in family.items():
    if age < 3:
        ticket_price = 0
    elif 3 <= age <= 12:
        ticket_price = 10
    else:
        ticket_price = 15

    print(f"{name} (age {age}) has to pay ${ticket_price}")
    
    total_cost += ticket_price

print(f"Total cost for the family: ${total_cost}")

# Exercises 3
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": {"pink", "green"}
    }
}

brand["number_stores"] = 2

print(f"Zara's clients include {', '.join(brand['type_of_clothes'])}.")

brand["country_creation"] = "Spain"

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

del brand["creation_date"]

print(f"The last international competitor is {brand['international_competitors'][-1]}.")

print("Major clothes colors in the US:", brand["major_color"]["US"])

print("Number of key-value pairs:", len(brand))

print("Keys of the dictionary:", list(brand.keys()))

more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}

print("More details on Zara:", more_on_zara)

brand.update(more_on_zara)

print("Value of 'number_stores':", brand['number_stores'])

# exercises 4
# 1
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
disney_users_A = {}

for i, user in enumerate(users):
    disney_users_A[user] = i

print(disney_users_A)

# 2
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
disney_users_B = {}

for i, user in enumerate(users):
    disney_users_B[i] = user

print(disney_users_B)

# 3
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
disney_users_C = {}

sorted_users = sorted(users)

for i, user in enumerate(sorted_users):
    disney_users_C[user] = i

print(disney_users_C)

# 4
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
disney_users_A = {}

for i, user in enumerate(users):
    if 'i' in user:
        disney_users_A[user] = i

print(disney_users_A)

# 5users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
disney_users_A = {}

for i, user in enumerate(users):
    if user[0] == 'm' or user[0] == 'p':
        disney_users_A[user] = i

print(disney_users_A)
