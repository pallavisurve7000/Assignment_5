# implement the complete student class

class Student:

    def getName(self):
        return self.name
    
    def setName(self,name):
        self.name = name

    def getRollNumber(self):
        return self.rollNumber
    
    def setRollNumber(self,rollNumber):
        self.rollNumber = rollNumber

student = Student()
name = input("Enter a name of student :")
rollno = input("Enter roll no of student :")
student.setName(name)
student.setRollNumber(rollno)

print("Name :",student.getName())
print("Roll number :",student.getRollNumber())
    