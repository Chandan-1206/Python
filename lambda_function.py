# lambda function

# def double(x):
    # return x*2
    
# function can be made by lambda too for one liner and is recommended to make for simple functions only
double = lambda x:x*2
print(double(15))    
avg=lambda x,y:(x+y)/2
print(avg(5,11))
info = lambda : print("Hi chandan")
info()

# We can also pass a function as a argument for another function like:-
def cube(x):
    return x**3
def ani(fx,value):
    return 2*fx(value)
print(ani(cube,5))

# so we can use this in lambda function too
print(ani(lambda x:x**3,5))
