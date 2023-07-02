# hybrid and hierarchical inheritance

# hybrid inheritance
# common structure:
class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass
# example:
class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def show_details(self):
    print("Name:", self.name)
    print("Age:", self.age)
    
class Person(Human):
  def __init__(self, name, age, address):
    Human.__init__(self, name, age)
    self.address = address
    
  def show_details(self):
    Human.show_details(self)
    print("Address:", self.address)
    
class Program(Human):
  def __init__(self, program_name, duration):
    self.program_name = program_name
    self.duration = duration
    
  def show_details(self):
    print("Program Name:", self.program_name)
    print("Duration:", self.duration)
    
class Student(Person,Program):
  def __init__(self, name, age, address, program,duration):
    Person.__init__(self, name, age, address)
    Program.__init__(self,program,duration)
    
  def show_details(self):
    Person.show_details(self)
    Program.show_details(self)
    
student = Student("John Doe", 25, "123 Main St.", "Computer Science","4 years")
student.show_details()
print("\n")

# heirarchical inheriatnce
# common structure:
class A:
    pass
class B(A):
    pass
class C(A):
    pass

# example:
class Animal:
    def __init__(self, name):
        self.name = name

    def show_details(self):
        print("Name:", self.name)

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name)
        self.breed = breed

    def show_details(self):
        Animal.show_details(self)
        print("Species: Dog")
        print("Breed:", self.breed)

class Cat(Animal):
    def __init__(self, name, color):
        Animal.__init__(self, name)
        self.color = color

    def show_details(self):
        Animal.show_details(self)
        print("Species: Cat")
        print("Color:", self.color)

dog = Dog("Max", "Golden Retriever")
dog.show_details()
cat = Cat("Luna", "Black")
cat.show_details()
