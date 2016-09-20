# Problem 9.9 (mystudent.py)
# Solution by Razvan Panea
# Date: 17.05.2013

from student import Student

class MyStudent(Student):

    def getFullName(self):
        return self.first + " " + self.last

student = MyStudent("Razvan", "Panea")
print(student.getFullName())
