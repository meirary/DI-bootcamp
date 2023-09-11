class Dog :

    def __init__(self, dog_name, dog_age, dog_color = "black", dog_energy = 100) :
        self.name = dog_name
        self.age = dog_age
        self.color = dog_color
        self.energy = dog_energy

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