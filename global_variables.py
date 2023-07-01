# Local and global variables
x=4
print(f"value of global variable is {x}")

def ram():
    z=5 # it gets destroyed when function returns
    print(f"value of local variable is {z}")
    global x # it will declare that this x is in global scope so that we can change the value in x by function
    x=17
    print(f"value of global variable in function is {x}")
    y=3
ram()
print(f"value of global variable is {x}")
# print(y) 
# this will cause an error because y is a local variable and is not accessible the function

# it is recommended to avoid using global keyword method as it makes harder to debbug the code 
# and reduces readability for later use.
