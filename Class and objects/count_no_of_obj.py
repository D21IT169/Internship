class Student :
    counter = 0

    def __init__(self,name,age) :
        self.name = name
        self.age = age
        Student.counter += 1

    def printDetails(self) :
        print(self.name,self.age,"years old")

    

student1 = Student('Ankit Rai',22)
student2 = Student('Aishwarya',21)
student3 = Student('Shaurya',21)
student4 = Student('Ankit Rai',22)
student5 = Student('Aishwarya',21)
student6 = Student('Shaurya',21)

print("Total number of objects created: ",Student.counter)
