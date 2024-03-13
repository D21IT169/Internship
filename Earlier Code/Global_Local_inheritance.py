# #Global in inheritance
x = 10 
class Emp():
	def __init__(self):
		print("Parent class", x)
		
class Freelance(Emp):
	def __init__(self):
		super().__init__()
	print("child class", x)
obj_free = Freelance()

print("-------------------------------------------------------------------")

#Local Variable of Parent class to child class
class Parent:
    def __init__(self):       
        self.x = 5
        print(self.x)

    def get_local(self):
        return self.x

class Child(Parent):
    def print_x(self):      
        print("Local Variable in Child Class:", self.get_local())

# Creating an instance of the child class
child_obj = Child()
child_obj.print_x()  	

print("------------------------------------------------------------------")

hetvi = 10                    #Global variable
class parent:
      def __init__(self):
            print("Global Variable in parent class",hetvi)
            self.x = 11  #Local variable
            print("Local Variable in parent class", self.x)

      def get_var(self):
            return self.x
            
class child(parent):
    def __init__(self):
          super().__init__()
          print("Global variable in child class", hetvi)

    def print_x(self):
           print("Local Variable in child class", self.get_var())
               
    
obj1 = child()  
obj1.print_x()
