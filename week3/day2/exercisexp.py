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

# Create instances of different cat breeds
bengal_cat = Bengal("Bengal Cat", 3)
chartreux_cat = Chartreux("Chartreux Cat", 4)
siamese_cat = Siamese("Siamese Cat", 2)

# Create a list of all cats
all_cats = [bengal_cat, chartreux_cat, siamese_cat]

# Create an instance of the Pets class with all the cats
sara_pets = Pets(all_cats)

# Take all the cats for a walk
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




