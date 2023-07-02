# Inheritance
class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def show(self):
        print(f"the name of employee :{self.id} is {self.name}")
class programmers(employee): #employee is inherited in programmers
    def showpro(self):
        print(f"programmer is occupation of {self.name}")

s1=employee("chandan",92)
s1.show()
s2=programmers("vanisha",87)
s2.show()
s2.showpro()
