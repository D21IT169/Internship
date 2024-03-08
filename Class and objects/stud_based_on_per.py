class Student:
    def getStudent(self):
        self.rollno = input("Enter Roll No: ")
        self.name = input("Enter Name: ")
        self.phy = int(input("Enter Physics Marks: "))
        self.chem = int(input("Enter Chemistry Marks: "))
        self.math = int(input("Enter Maths Marks: "))
        self.result()

    def putStudent(self):
        print("Roll Number: ", self.rollno, end = " ")
        print("Name: ", self.name, end = " ")
        print("Percentage: ", self.percentage, end = " ")
        if (self.percentage >= 60):
            print("Pass")
        else:
            print("Fail")

    def result(self):   
        total = self.phy + self.chem + self.math
        self.percentage = (int)(total / 3)
            
    def search(self,min,max):
         if(self.percentage>=min and self.percentage<=max):
             return True
         else:
             return False

studentList = list()

while(True):
    studentObject=Student()
    studentObject.getStudent()
    studentList.append(studentObject)
    ch=input("Continue y/n? ")
    if ch == 'n':
        break
    
min=int(input("Enter Min Perc: "))
max=int(input("Enter Max Perc: "))

searchList = list()

for studentObject in studentList:
    found=studentObject.search(min,max)
    if(found):
        searchList.append(studentObject)
if(len(searchList)==0):
    print('No Record Exist')
else:
 
 for studentObject in searchList:
     studentObject.putStudent()
