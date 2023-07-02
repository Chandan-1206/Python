# multiple inheritance
class employee:
    def __init__(self,name):
        self.name=name
    
    def show(self):
        print(f"name is {self.name}")

class martial_art:
    def __init__(self,form):
        self.form=form
    
    def show(self):
        print(f"martial art form is {self.form}")

class person(employee,martial_art):
    def __init__(self,name,form):
        self.name=name
        self.form=form

p=person("vidyut jamwal","kalari payattu")
p.show() # this will execute method of class inherited at first place 

# mro(method resolution order) method
print(person.mro()) # mro tells the order of priority for same name methods to be execurted
