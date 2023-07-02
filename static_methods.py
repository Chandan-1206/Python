# static methods
class math:
    def __init__(self,num):
        self.num=num
    
    def addtonum(self,num2): # function in class without staticmethod
        self.num=self.num+num2
    @staticmethod # We use staticmethod to associate a function to a class and here we don't have to use self as it is not associated to object
                  # hence we can also use class name to call it.
    def add(a,b):
        return a+b

obj = math(20)
print(obj.num)
obj.addtonum(10)
print(obj.num)
print(obj.add(9,1))
print(math.add(9,1))
# This is not a replacement for general functions we can still make them outside of class too but is just a way too associate a function to class 
# if we want that user of that class can use that function independent of class variables
