class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, animal, quantity=1):
        if animal in self.animals:
            self.animals[animal] += quantity
        else:
            self.animals[animal] = quantity

    def get_info(self):
        info = f"{self.name}'s farm\n"
        sorted_animals = sorted(self.animals.items())
        for animal, quantity in sorted_animals:
            info += f"{animal} : {quantity}\n"
        info += "E-I-E-I-0!"
        return info

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        animal_types = self.get_animal_types()
        animal_list = ", ".join(animal_types)
        return f"{self.name}'s farm has {animal_list}."


# Testing the code
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_short_info())
