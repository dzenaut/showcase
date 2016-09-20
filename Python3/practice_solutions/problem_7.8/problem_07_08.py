# Problem 9.8
# Solution by Razvan Panea
# Date: 17.05.2013

class Student:

    def __init__(self, first, last):
        self.first = first
        self.last = last

class MyStudent(Student):

    def getFullName(self):
        return self.first + " " + self.last

student = MyStudent("Razvan", "Panea")
print(student.getFullName())
