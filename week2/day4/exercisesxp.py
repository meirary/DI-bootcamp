 # exercises 1

def display_message():
    message = "I am learning to code at Developers Institute."
    print(message)

display_message()

# Exercises 2

def favorite_book(title):
    message = f"One of my favorite books is {title}."
    print(message)

favorite_book("Alice in Wonderland")

 # Exercises 3 

def describe_city(city, country):
    print(f"{city} is in {country}.")


describe_city("Reykjavik", "Iceland")
describe_city("New York", "United State")


# Exercises 4

import random

def compare_numbers(user_number):
    if 1 <= user_number <= 100:
    
        random_number = random.randint(1, 100)

        if user_number == random_number:
            print("Success! You guessed number.")
        else:
            print(f"Fail! Your number: {user_number}, Random number: {random_number}")
    else:
        print("Please enter a number between 1 and 100.")

user_input = int(input("Enter a number between 1 and 100: "))
compare_numbers(user_input)

# Exercise 5

def make_shirt(size="large", text="I love Python"):
    message = f"The size of the shirt is {size} and the text is '{text}'."
    print(message)

make_shirt()  
make_shirt("medium")  
make_shirt("small", "I'm the best on Python!") 

# Exercises 6

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = "the Great " + magicians[i]

make_great(magician_names)
show_magicians(magician_names)

 # Exercises 7

import random

def get_random_temp(season):
    if season == "winter":
        lower_limit, upper_limit = -10, 16
    elif season == "spring" or season == "autumn" or season == "fall":
        lower_limit, upper_limit = 0, 23
    elif season == "summer":
        lower_limit, upper_limit = 24, 40
    else:
        print("Invalid season. Defaulting to all seasons.")
        lower_limit, upper_limit = -10, 40

    return round(random.uniform(lower_limit, upper_limit), 2)

def provide_advice(temperature):
    if temperature < 0:
        return "Brrr, that’s freezing! Wear some extra layers today."
    elif 0 <= temperature <= 16:
        return "Quite chilly! Don’t forget your coat."
    elif 16 < temperature <= 23:
        return "Nice weather today!"
    elif 24 <= temperature <= 32:
        return "Warm day! Enjoy the sunshine."
    else:
        return "Hot day! Stay hydrated."

def main():
    month = int(input("Enter the month (1-12): "))
    if 1 <= month <= 12:
        if 3 <= month <= 5:
            season = "spring"
        elif 6 <= month <= 8:
            season = "summer"
        elif 9 <= month <= 11:
            season = "autumn"
        else:
            season = "winter"
        
        temperature = get_random_temp(season)
        advice = provide_advice(temperature)

        print(f"The temperature right now is {temperature} degrees Celsius.")
        print(advice)
    else:
        print("Invalid month. Please enter a number between 1 and 12.")

main()

# Exercises 5b or 8

data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]


def star_wars_quiz(questions):
    correct_answers = 0
    incorrect_answers = 0
    wrong_answers = []

    for question_data in questions:
        question = question_data["question"]
        correct_answer = question_data["answer"]
        user_answer = input(f"{question}: ")

        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Incorrect. The correct answer is: {correct_answer}")
            incorrect_answers += 1
            wrong_answers.append({
                "question": question,
                "user_answer": user_answer,
                "correct_answer": correct_answer
            })

    print(f"\nNumber of Correct Answers: {correct_answers}")
    print(f"Number of Incorrect Answers: {incorrect_answers}")

    if incorrect_answers > 3:
        print("\nYou got more than 3 answers wrong. Please play again.")
        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again == "yes":
            star_wars_quiz(data)
        else:
            print("Thanks for playing!")

    if incorrect_answers > 0:
        print("\nQuestions You Answered Incorrectly:")
        for wrong_answer in wrong_answers:
            print(f"Question: {wrong_answer['question']}")
            print(f"Your Answer: {wrong_answer['user_answer']}")
            print(f"Correct Answer: {wrong_answer['correct_answer']}")
            print()

star_wars_quiz(data)
