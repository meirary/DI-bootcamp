#  Exercises 1

class Family:
    def __init__(self, last_name, initial_members_data):
        self.last_name = last_name
        self.members = initial_members_data
        self.animals = []

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

    def born(self, **kwargs):
        new_child = {'name': kwargs.get('name', 'Unknown'), 'age': kwargs.get('age', 0),
                     'gender': kwargs.get('gender', 'Unknown'), 'is_child': True}
        self.members.append(new_child)
        print(f"Congratulations! {new_child['name']} is born into the {self.last_name} family.")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False

    def family_presentation(self):
        print(f"The {self.last_name} family members:")
        for member in self.members:
            print(member['name'])


class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


initial_members_data = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
]

my_family = Family('Smith', initial_members_data)

my_family.born(name='Teresa', age=0, gender='Female')
print(f"Is Michael over 18? {my_family.is_18('Michael')}")
my_family.family_presentation()

# exercises 2

class TheIncredibles(Family):
    def __init__(self, last_name, initial_members_data):
        super().__init__(last_name, initial_members_data)

    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] >= 18:
                    print(f"{name}'s power is {member['power']}")
                else:
                    raise Exception(f"{name} is not over 18 years old.")

    def incredible_presentation(self):
        super().family_presentation()
        print("Incredible Names and Powers:")
        for member in self.members:
            print(f"{member['name']} - Incredible Name: {member['incredible_name']}, Power: {member['power']}")

initial_incredibles_data = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
]

incredibles_family = TheIncredibles('Incredible', initial_incredibles_data)

incredibles_family.incredible_presentation()

incredibles_family.born(name='Jack', age=2, gender='Male', power='Unknown Power', incredible_name='Incredible Jack')

incredibles_family.incredible_presentation()
