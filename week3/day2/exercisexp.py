# Exercises 1

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'


bengal_cat = Bengal("Bengal Cat", 3)
chartreux_cat = Chartreux("Chartreux Cat", 9)
siamese_cat = Siamese("Siamese Cat", 1)


all_cats = [bengal_cat, chartreux_cat, siamese_cat]

sara_pets = Pets(all_cats)


sara_pets.walk()

# Exercises 2

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight / (self.age * 10)

    def fight(self, other_dog):
        self_speed = self.run_speed() * self.weight
        other_speed = other_dog.run_speed() * other_dog.weight

        if self_speed > other_speed:
            return f"{self.name} won the fight"
        elif other_speed > self_speed:
            return f"{other_dog.name} won the fight"
        else:
            return "It's a draw"

dog1 = Dog("Rex", 3, 25)
dog2 = Dog("Buddy", 4, 30)
dog3 = Dog("Didi", 6, 23)

print(dog1.bark()) 
print(dog2.run_speed())  
print(dog1.fight(dog3)) 


# Exercises 3

import random


class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")


class PetDog(Dog):
    def __init__(self, name, breed):
        super().__init__(name, breed)
        self.trained = False

    def train(self):
        super().bark()
        self.trained = True

    def play(self, *dog_names):
        print(f"{', '.join(dog_names)} all play together")

    def do_a_trick(self):
        if self.trained:
            trick = random.choice([
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ])
            print(trick)
        else:
            print(f"{self.name} is not trained yet.")


if __name__ == "__main__":
    pet_dog = PetDog("Perrito", "Golden Retriever")
    pet_dog.train()
    pet_dog.play("Popo", "Max")
    pet_dog.do_a_trick()
