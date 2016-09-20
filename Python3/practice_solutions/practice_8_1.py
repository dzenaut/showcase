from student import Student

class GradedStudent:
    student = None
    grade  = None
    def __init__(self, newStudent):
        self.student  = newStudent

    def getGrade(self):
        return self.grade

    def setGrade(self, newGrade):
        self.grade = newGrade

#b = Student("Andrei","Iancu")
#a = GradedStudent(b)
#a.setGrade(7.8)
#print a.getGrade()

