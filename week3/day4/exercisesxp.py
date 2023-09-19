# Exercises 1

import random

def get_words_from_file(file_name):
    with open(file_name, 'r') as file:
        words = file.read().splitlines()
    return words

def get_random_sentence(length, words):
    random_words = random.sample(words, length)
    sentence = ' '.join(random_words).lower()
    return sentence


def validate_sentence_length(input_value):
    try:
        length = int(input_value)
        if 2 <= length <= 20:
            return length
        else:
            print("Sentence length must be between 2 and 20.")
            return None
    except ValueError:
        print("Invalid input. Please enter an integer between 2 and 20.")
        return None

def main():
    print("Random Sentence Generator")
    while True:
        sentence_length = input("Enter the desired sentence length (between 2 and 20): ")
        validated_length = validate_sentence_length(sentence_length)
        if validated_length is not None:
            break

    words = get_words_from_file("word_list.txt")  
    if words:
        sentence = get_random_sentence(validated_length, words)
        print(f"Random Sentence ({validated_length} words): {sentence}")

if __name__ == "__main__":
    main()


# exercises 2

import json

sampleJson = """{
   "company": {
      "employee": {
         "name": "emma",
         "payable": {
            "salary": 7000,
            "bonus": 800
         }
      }
   }
}"""

data = json.loads(sampleJson)

salary = data["company"]["employee"]["payable"]["salary"]
print("Salary:", salary)


data["company"]["employee"]["birth_date"] = "01-01-1990" 


with open("modified_data.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

print("Modified data saved to 'modified_data.json'")
