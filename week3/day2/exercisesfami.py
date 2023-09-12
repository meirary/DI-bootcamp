class Family():
    def __init__(self, name, age, gender, ischild):
        self.name = name
        self.age = age
        self.gender = gender


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


# Initial members data
initial_members_data = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
]

# Create a Family instance
my_family = Family('Smith', initial_members_data)

# Test the methods
my_family.born(name='Emma', age=0, gender='Female')
print(f"Is Michael over 18? {my_family.is_18('Michael')}")
my_family.family_presentation()
