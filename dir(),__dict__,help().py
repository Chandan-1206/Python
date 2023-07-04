# dir method,__dict__ attribute and help method

# dir()
x=[1,2,3]
print(dir(x))
# returns all methods of a variable/object

# __dict__
class student:
    def __init__(self,name,enroll):
        self.name=name
        self.enroll=enroll
s=student("chandan",92)
print("\n",s.__dict__)
# makes a dictionary of all attributes and their data

# help()
# print(help(str))
print(help(student))
# print(help(s))
#gives a discription of all methods and attributes of an object
