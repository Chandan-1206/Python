# instance variables vs class variables

# why we use self in non argument method too ?
class employee:
    company='google' # this is a class variable as it is made out side of any method and will be same for every object 
    # until object have an instance variable and class variable can also be changed by using classname
    no_of_emp=0 # good example of class variable as this number of employees can't be associated to objects
    def __init__(self,name):
        self.name=name 
        self.raise_amt=0.2  # these are instance variables associated to an object and are made in a method
        employee.no_of_emp+=1 # classname is used as class variable is used
    def show(self):
        print(f"In {self.company} with {self.no_of_emp} employees,the employee name is {self.name} and raise amount is {self.raise_amt}")
        
    # def noarg(): # this will give TypeError: employee.noarg() takes 0 positional arguments but 1 was given bcz a.noarg() can be 
    # written as employee.noarg(a) they are same so now we gave a argument here but in function we didn't initialized it
    def noarg(self):
        print("this is a non argument method")
        

a=employee('chandan') 
a.show()
a.noarg()
employee.noarg(a) # this is same as above line and shows that how one argument is given here
employee.company='amazon' # this will change data of class variable for every instance
b=employee('nishchay')
b.raise_amt=0.5 # we can change it by using object ONLY as it was instance variable
b.show()
c=employee('jaadu')
c.company='microsoft' # now this is treated as an instance variable and is considered before class variable
c.show()
d=employee('vanisha')
d.show()
