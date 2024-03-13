# print("Hello")
# x = 5
# print(x)


# # Global variable
# global_var = "I am a global variable"

# class ParentClass:
#     def __init__(self):
#         self.local_var = "I am a local variable in ParentClass"
    
#     def print_variables(self):
#         print("Global variable:", global_var)
#         print("Local variable:", self.local_var)

# class ChildClass(ParentClass):
#     pass  # Inherits from ParentClass

# # Create an instance of ChildClass
# child_obj = ChildClass()

# # Access and print variables
# child_obj.print_variables()


class Parent:
    def __init__(self):
        # Local variable in the parent class constructor
        self.local_var_parent = 5

class Child(Parent):
    def __init__(self):
        # Call the __init__ method of the parent class
        Parent.__init__(self)

        # Accessing local variable in the parent class directly
        print("Local Variable in Parent Class (from Child Class):", self.local_var_parent)

# Creating an instance of the child class
child_obj = Child()





#  def transfer(self, recipient, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             recipient.set_balance(recipient.get_balance() + amount)
#             print(f'Transfer successful. Current Balance: ₹{self.__balance}')
#         else:
#             print('Invalid amount or insufficient balance. Transfer aborted.')
