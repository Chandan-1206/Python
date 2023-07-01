# default arguments
def avg(a=0,b=0):
    if(b==0):
        b=a
    elif(a==0):
        a=b
    print((float)(a+b)/2)
x=int(input("enter first number: "))
y=int(input("enter second number: "))
avg(x,y)
# required arguments
def add(m,n):
    return m+n
print(add(23,58))    
