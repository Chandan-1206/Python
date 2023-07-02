# decorators
# for no argument function
def greet(fx):
    def mfx():
        print("good morning")
        fx()
        print("tnx for using function")
    return mfx
@greet
def hello():
    print("hello bonbon")

hello()

# for function with arguments
def salute(fy):
    def nfy(args,*kwargs):
        print("good morning")
        fy(args,*kwargs)
        print("tnx for using function")
    return nfy
    
@salute
def add(x,y):
    print (x+y)
add(5,10)    

# @salute   # this is also correct
def square(x):
    print(x**2)
salute(square)(5)
# above(@ method) was shorthand of this syntax
def cube(x):
    print(x**3)
cube=salute(cube)
cube(4)
