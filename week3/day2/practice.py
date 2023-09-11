# Exercise

# Using the Employee class of yesterday

# 1. Create a Developer class, that inherits from the Employee class with the attributes :
# - firstname, lastname, age,
# - job is developer as 
# default,
# - salary is 15000 by default,
# - coding skills (a list by default) : all developers should start with an empty list of skills

# 2. Create 2 developers objects and display their attribute
# - Tom Cruiz 30 years old
# - Angelina Jolie 23 years old

# 3. Add those methods to the class

# - add_skills(self, *skills) : receives a tuple of skills and append them to the coding skills list
# - coding(self) : print a nice sentence with all the coding languages the developer knows
# - coding_with_partner(self, other_developer) : print a nice sentence with the name of both developers, and their skills
# - override the get_promotion(self, promotion_amount) : that multiplies the salary of the user by the promotion

# 4. Call all the methods, also those from the Employee Class

class Employee :
    def __init__(self, firstname, lastname, age, job, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.job = job
        self.salary = salary
    
    def get_fullname(self) :
        return f"{self.firstname} {self.lastname}"
    
    def happy_birthday(self):
        self.age += 1
    
    def get_promotion(self, new_promotion) :
        self.salary += new_promotion

    def show_info (self) :
        print(f"{self.get_fullname()} is {self.age} years old, his job is {self.job} and his salary is {self.salary}")
    

    
lst_names = ["John", "Lea", "Emma", "Josh", "Eli"]
lst_lastnames = ["Cohen", "Smith", "Doe", "Sevi", "Swtazh"]
lst_jobs = ["developer", "dancer", "cowboy", "tennis player", "doctor"]
--> random age from 18 to 67
--> random salary from 10000 to 45000