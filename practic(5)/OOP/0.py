# OOП 1 (0,3) ІНДЗ 2 (1)

#import person
#from person import Student
#import person as p
from person import *

class Course:
    def __init__(self):
        self.id = ''
        self.title = ''
        self.credit = 0
        self.teachers = []

class Department:
    def __init__(self):
        self.title = ''
        self.teachers = []
        self.courses = []

departament = Department()
departament.title = '...'
departament.teachers = [ Teacher('Bob', 'Bob', 5) ]

student = Student('Zhenya', 'Tertychniy', 16, 'CHSBC', 2020, 100, departament)
print(student)