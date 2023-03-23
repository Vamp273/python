class student:
    numberOfSubjects = 5
# static method = it does not depend on any object
# self = pointer which points towards the class i.e. calling it 
    def __init__(self, marks1, marks2, marks3):
        self.web = marks1
        self.python = marks2
        self.math = marks3

    def average(self):
        return ((self.web + self.python + self.math)/3)

    def getMarks(self):  # Accessors
        return self.math

    def getMarks(self,marks):  # mutators
        self.math = marks


    @classmethod
    def ClassMethodExample(cls):
        return cls.numberOfSubjects

    @staticmethod
    def staticMethodEx():
        print("This is an example of static method.")

student1 = student(5,4,6)
student2 = student(7,8,9)
student3 = student(6,7,8)

print(student1.web, student1.python, student1.math)
print(student2.web, student2.python, student2.math)
print(student3.web, student3.python, student3.math)

print("Average of marks of student1 : ", student1.average())
print("Average of marks of student2 : ", student2.average())
print("Average of marks of student3 : ", student3.average())

print(student.ClassMethodExample())

student.staticMethodEx()

