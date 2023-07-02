# Magic/Dunder methods 

# __init__ is also a dunder method which is used to make constructors

# __len__ 
class employee:
    name="chandan"
    def __len__(self):
        # we can also use len(self.name) but this is raw code to get length of a string
        i=0
        for j in self.name:
            i+=1
        return i    

e=employee()
print(e.name)
print(len(e)) # this is calling __len__ thats why it is also called magic methods

# __str__ or __repr__

# these are used to provide string representation of an object 
# they should be used as:
# __str__ gives a informal(user friendly) representation
# __repr__ gives a formal (developer friendly) representation

class student:  
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return f"the name of the student is {self.name}"
    def __repr__(self):
        return f"Student:'{self.name}'"
    def __call__(self): # can be called by instances as methods 
        print("this is student class and is used to store info of students")
# this is mainly used when a class is imported and used in other program 
s=student("chandan")
print(str(s)) # if we haven't made __str__ then it will also call __repr__ 
print(repr(s)) # if we haven't made __repr__ it ll automatically give formal info

    
#__call__
# __call__ turns instances(objects) into callable methods
s()
# methods such as _add_ and _mul_ are also dunder methods which are used in operator overloading in python.
