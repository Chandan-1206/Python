# raising custom errors -> raise keyword (similar to throw in c++)
a=int(input("enter the value between 3 and 10 : "))
if(a<3 or a>10):
    raise ValueError("the value is not between 3 and 10 !!!")
    
print(f"the value of a is {a}")    
#we can give predefined errors in raise or can create our own errortype class
