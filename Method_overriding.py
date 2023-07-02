# Method overriding 
class shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        return self.x*self.y
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
        super().__init__(radius,radius)
    def area(self): 
    # making same name function in subclass and then making child class object ll call child class function this is overriding 
    # instead of doing the below stuff we can use super
    # return 3.14*self.radius**2
        return 3.14*super().area()
s=shape(4,5)
print(s.area())
c=circle(5)
print(c.area())
