example

class Employee : 
    def __init__(self) -> None:
        pass

class Student :

    school_name = "DevelopersInstitute"

    def __init__(self, name, level) :
        self.name = name
        self.level = level

    # instance method
    def do_exams(self, test_name) :
        print(f"{self.name} is doing a {test_name} exam")

    @classmethod
    def create_new_student(cls, grade) :
        print(cls.school_name)
        if grade == "A" :
            new_student_name = input("Your name \n")
            new_student_level = input("Your level \n")
            return cls(new_student_name, new_student_level) 
            # creating a new student
            # Student("John", "1st")
    

class BestStudent(Student) :
    pass


new_student = BestStudent.create_new_student("A")
print(new_student)

