class Class1:
	def m(self):
		print("Hey from Class1") 
	
class Class2(Class1):
	def m(self):
		print("Hey from Class2")
		Class1.m(self)

class Class3(Class1):
	def m(self):
		print("Hey from Class3")
		Class1.m(self) 
	
class Class4(Class2, Class3):
	def m(self):
		print("Hey from Class4") 
		Class2.m(self)
		Class3.m(self)
	
obj = Class4()
obj.m()
