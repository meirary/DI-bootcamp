# Exercises 3
from exercisexp import Dog 
import random

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        bark_output = super().bark()
        self.trained = True
        print(bark_output)
        print(f"{self.name} is now trained!")

    def play(self, *dog_names):
        dog_names_str = ", ".join(dog_names)
        print(f"{dog_names_str} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            random_trick = random.choice(tricks)
            print(random_trick)
        else:
            print(f"{self.name} is not trained yet. Train the dog first.")

# Example usage:
if __name__ == "__main__":
    pet_dog = PetDog("Buddy", 3, 25)

    pet_dog.train()  # Trains the dog
    pet_dog.play("Rex", "Max", "Luna")  # Dogs play together
    pet_dog.do_a_trick()  # Performs a random trick if trained
