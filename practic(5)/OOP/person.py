
class Person:
    first_name = ''
    second_name = ''
    age = 0
    
    def __init__(self, first_name, second_name, age):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age

    def __str__(self):
        return f'Привіт, мене звати {self.first_name} {self.second_name}'

class Teacher(Person):
    courses = []

class Student(Person):
    school = ''
    yearEntry = 0
    gpa = 0
    department = ''

    def __init__(self, first_name, second_name, age, school, yearEntry, gpa):
        super().__init__(first_name, second_name, age)
        self.school = school
        self.yearEntry = yearEntry
        self.gpa = gpa

    def __str__(self):
        return f'first name: {self.first_name}\nsecond name: {self.second_name}\nage:{self.age}\nschool:{self.school}\nyearEntry:{self.yearEntry}\nGPA: {self.gpa}'
