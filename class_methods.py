# Class methods
class employee:
    company='apple'
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"{self.name} is in {self.company} company")
    
    @classmethod # this will make this function a classmethod
    def changecomp(cls,newcomp): # by default cls,self or any other variable as first argument will take instance as the given argument
    # and will not change the name for whole class until we use classmethod decorator    
        cls.company=newcomp
        

a=employee('chandan')
a.show()
a.changecomp('google') # this will just change the company for a instance if we don't use classmethod
a.show()
b=employee('vanisha')
b.show()
employee.changecomp('microsoft') #this will not work until we make the function classmethod
c=employee('nishchay')
c.show()
d=employee('jaadu')
d.show()
