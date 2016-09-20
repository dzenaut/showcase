from student import Student
from gradedStudent import GradedStudent
from course import Course

class AverageableCourse(Course):

    def getAverage(self):
        avg = 0.0
        for s in self.students:
            avg = avg + s.getGrade()
        avg = avg / len(self.students)
        return avg

#a = Student("aaa","aa")
#gradedA = GradedStudent(a)
#b = Student("bbb","bb")
#gradedB = GradedStudent(b)
#course = AverageableCourse("catalogue")
#course.addStudent(gradedA)
#course.addStudent(gradedB)
#course.setGrade(gradedA,8.8)
#course.setGrade(gradedB,9.2)
#print course.getAverage()
