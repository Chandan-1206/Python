# constructors
class temp:
# _init_ is used in python to make constructors
    def __init__(self): # it is a default constructor as it doesn't takes arguments except self
        print("it will be called automatically when an object is made")
    
a=temp()

class students:
    def __init__(self,name,age): # it is a parameterized constructor used for initializing values
        self.name=name
        self.age=age
    def show(self):
        print(f"{self.name} is of {self.age} years old")
obj=students("froggie",18)
obj.show()
