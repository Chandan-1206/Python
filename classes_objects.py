# classes and objects
class student:
    name="name"
    age=00

obj1=student() # making object for the class student
obj1.name="chandan"
obj1.age=19
print(f"{obj1.name} is of {obj1.age} years old\n") # we have to repeat it do we can make a function for it

# self keyword
class friends:
    name="monica" # these are default values if not changed then they will be used 
    age=28
    def info(self): # self is refered to the object for which function is called
        print(f"{self.name} is of {self.age} years old")

a=friends()
b=friends()
c=friends()
d=friends()
a.name="joey"
b.name="pheoby"
c.name="chandler"
a.age=25
b.age=26
c.age=25
a.info()
b.info()
c.info()
d.info()
