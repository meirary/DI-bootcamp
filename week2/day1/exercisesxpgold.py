# Exercises 1
print(("Hello world\n" * 4 + "I love python\n" * 4).strip())

# Exercises 2
month = int(input("Enter a month (1 to 12): "))

seasons = {
    3: "Spring",
    4: "Spring",
    5: "Spring",
    6: "Summer",
    7: "Summer",
    8: "Summer",
    9: "Autumn",
    10: "Autumn",
    11: "Autumn",
    12: "Winter",
    1: "Winter",
    2: "Winter",
}

if 1 <= month <= 12:
    season = seasons[month]
    print(f"The season for month {month} is {season}.")

