# OOП 1 (0,3) ІНДЗ 2 (1)

#import person
#from person import Student
#import person as p
from person import *

class Course:
    id = ''
    title = ''
    credit = 0
    teachers = []

class Department:
    title = ''
    teachers = []
    courses = []

student = Student('Zhenya', 'Tertychniy', 16, 'CHSBC', 2020, 100)
print(student)