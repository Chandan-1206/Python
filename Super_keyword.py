# Super keyword
class parent:
    def parentfun(self):
        print("this is parent class function")

class child(parent):
    def parentfun(self):
        print("this is child class's parent function")
    def childfun(self):
        print("this is child class")
        super().parentfun() # super keyword is used to call parent class function kind of like overriding in c++.
a=child()
a.childfun()
a.parentfun() # if parentfun would not exist in child class then by normal inheritance parent class's function will be called.


class employee:
    def __init__(self,name,idno):
        self.name=name
        self.idno=idno
class programmer(employee):
    def __init__(self,name,idno,lang):
        #now instead of writting code for name and idno again i can use parent class's constructor bcz of inheritance using super
        super().__init__(name,idno)
        self.lang=lang

e=employee("nishchay",83)
p=programmer("jaadu",84,"c++")
print(e.name,e.idno)
print(p.name,p.idno,p.lang)
