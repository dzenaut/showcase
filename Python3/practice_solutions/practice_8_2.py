from student import Student
from gradedStudent import GradedStudent

class Course:
    title = None
    student = None
    def __init__(self,newTitle):
        self.title = newTitle
        self.students  = []

    def addStudent(self,newStudent):
        self.students.append(newStudent)

    def setGrade(self, student, grade):
        num = self.students.index(student)
        self.students[num].setGrade(grade)


#a = Student("aaa","aa")
#gradedA = GradedStudent(a)
#b = Student("bbb","bb")
#gradedB = GradedStudent(b)
#course = Course("catalogue")
#course.addStudent(gradedA)
#course.addStudent(gradedB)
#course.setGrade(gradedA,8.8)



