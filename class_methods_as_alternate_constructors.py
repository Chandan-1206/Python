# class methods as alternate constructors
class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @classmethod
    def fromstring(cls,string): # this works as an alternate constructor
        return cls(string.split('-')[0],int(string.split('-')[1]))

e1=employee("chandan",1200000)
print(e1.name)
print(e1.salary)

# if we are given data in string form like 
st1="shivansh-1500000"
# we can use split 
e2=employee(st1.split('-')[0],int(st1.split('-')[1]))
print(e2.name)
print(e2.salary)
# but this reduces readability and is lengthy when we use many objects , so to make it tidy here we can use classmethods 
# and make additional constructors from it
st2="nishchay-1300000"
e3=employee.fromstring(st2) 
print(e3.name)
print(e3.salary)
