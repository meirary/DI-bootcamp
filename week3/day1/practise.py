class Dog :

    def __init__(self, name, age, color = "black", energy = 100) :
        self.name = name
        self.age = age
        self.color = color
        self.energy =  energy

    # method happybirthday increment the age by one
    def happy_birthday(self) :
        self.age += 1

    def show_info (self) :
        print(f"The dog name is {self.name}, his age is {self.age}, he is of color {self.color}")

    def go_to_groomer(self, owner_color) :
        self.color = owner_color

    def play (self, activity) :
        if self.energy >= 10:
            if self.energy >= 10 and activity == "ball" :
                self.energy -= 10
                print(f"{self.name} is playing ball - he has {self.energy} energy left")
            elif self.energy >= 30 and activity == "frisbee":
                self.energy -= 30
                print(f"{self.name} is playing frisbee - he has {self.energy} energy left")
            elif self.energy >= 70 and activity.energy >= 70 and isinstance(activity, Dog) :
                self.energy -= 70 #lea_dog energy
                activity.energy -= 70 #activity is dan_dog
                print(f"{self.name} and {activity.name} are playing together - {self.name} has {self.energy} energy left - - {activity.name} has {activity.energy} energy left")
            else :
                print(f"You have {self.energy} left - You don't have enough energy to play {activity} \n")
                self.play(input("Please choose another activity between ball, frisbee and play date \n"))
        else :
            self.sleep()
    
    def sleep (self) :
        self.energy = 100
        print(f"{self.name} slept, he has {self.energy} energy")

lea_dog = Dog("Spock", 2)
dan_dog = Dog("Rex", 4, "white")
lea_dog.play(dan_dog)

class Dog : 
    
    def __init__(self, name, color, age) :
        self.name = name
        self.color = color
        self.age = age

    def bark(self) :
        print("Woof")

    # pleasing sentence informing the user of the information
    # called when we print the object
    def __str__(self) :
        return f"the dog name is {self.name}, the dog color is {self.color}"

    # straight to the point sentence 
    # inform the developer of the information
    # called in the python shell while calling the object
    # >>> my_dog
    def __repr__(self):
        return f"name : {self.name} color : {self.color}"
    
    # the 2 parameters are objects
    def __gt__(self, other_dog) :
        if self.age > other_dog.age :
            print(f"{self.name}  is bigger than {other_dog.name}")
            return self
        else :
            print(f"{other_dog.name}  is bigger than {self.name}")
            return other_dog
    
    # add 2 dogs together
    # return the new puppy that was conceived
    def __add__(self, other_dog) :
        puppy_name = input("what is the name of the new puppy")
        puppy_color = f"{self.color} {other_dog.color}"
        print("a new puppy is born")
        return Dog(puppy_name, puppy_color, 0)
    
my_dog = Dog("rex", "black", 12)
my_friend_dog = Dog("lola", "brown", 2)
print(my_dog > my_friend_dog)
# calling the str dunder method
# the dog name is rex, the dog color is black
# print(my_dog)
new_puppy = my_dog + my_friend_dog
new_puppy.bark()














