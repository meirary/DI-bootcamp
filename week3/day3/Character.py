class Character:
    def __init__(self, name):
        self.name = name
        self.life = 20
        self.attack = 10

    def basic_attack(self, other_char):
        other_char.life -= self.attack

class Druid(Character):
    def __init__(self, name):
        super().__init__(name)
        print(f"Druid {self.name} has been created!")

    def meditate(self):
        self.life += 10
        self.attack -= 2

    def animal_help(self):
        self.attack += 5

    def fight(self, other_char):
        damage = 0.75 * self.life + 0.75 * self.attack
        other_char.life -= damage

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name)
        print(f"Warrior {self.name} has been created!")

    def brawl(self, other_char):
        damage = 2 * self.attack
        self.life += 0.5 * self.attack
        other_char.life -= damage

    def train(self):
        self.attack += 2
        self.life += 2

    def roar(self, other_char):
        other_char.attack -= 3

class Mage(Character):
    def __init__(self, name):
        super().__init__(name)
        print(f"Mage {self.name} has been created!")

    def curse(self, other_char):
        other_char.attack -= 2

    def summon(self):
        self.attack += 3

    def cast_spell(self, other_char):
        damage = self.attack / 5  # Modify this formula as needed
        other_char.life -= damage

# Testing the characters and their methods
druid = Druid("Gandalf")
warrior = Warrior("Aragorn")
mage = Mage("Merlin")

druid.meditate()
druid.animal_help()
druid.fight(warrior)

warrior.brawl(druid)
warrior.train()
warrior.roar(druid)

mage.curse(warrior)
mage.summon()
mage.cast_spell(druid)

print(f"{druid.name}'s life: {druid.life}, attack: {druid.attack}")
print(f"{warrior.name}'s life: {warrior.life}, attack: {warrior.attack}")
print(f"{mage.name}'s life: {mage.life}, attack: {mage.attack}")
