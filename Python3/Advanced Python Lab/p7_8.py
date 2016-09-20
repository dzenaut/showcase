class Student:
    def __init__(self, first, last):
        self.first = first
        self.last = last

class NewStudent(Student):
    def getFullName(self):
        return self.first + " " + self.last

#10.1

class GradedStudent():
    def __init__(self,student):
        '''student is an instance of the class Student.'''
        self.student = student
        self.grade = None

    def getGrade(self):
        return self.grade

    def setGrade(self,grade):
        '''grade is a float'''
        self.grade = grade

class Course():
    def __init__(self,title):
        '''title is a string'''
        self.title = title
        self.students = []

    def addStudent(self,student):
        '''student is an instance of the class GradedStudent'''
        self.students.append(student)

    def setGrades(self, student, grade):
        '''student is an instance of the class GradedStudent, grade is a float'''
        student.setGrade(grade)

class AveragableCourse(Course):
    def getAverageGrade(self):
        sumgrade = 0
        for student in self.students:
            sumgrade += float(student.getGrade())
        average = sumgrade/len(self.students)
        return average

dboi = NewStudent("Dennis", "Ledwon")
print(dboi.getFullName())
gradedboi = GradedStudent(dboi)

p1 = AveragableCourse("Introduction to Python")
p1.setGrades(gradedboi, 1.0)
p1.addStudent(gradedboi)
print(p1.getAverageGrade())

