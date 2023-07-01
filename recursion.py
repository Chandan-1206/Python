# recursion
def factorial(n):
    if(n==0):
        return 1
    else:
        return n*factorial(n-1)

n=int(input("enter the no. to get its factorial : "))
print("the factorial of",n,"=",factorial(n))

def fibonacci(n):
    if(n==1):
        return 0
    elif(n==2):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

m=int(input("enter the number for fibonacci series : "))
print(fibonacci(m))
