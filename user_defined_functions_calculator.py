# user defined functions - calculator lite 
def add(a,b):
    print (a+b)
def sub(a,b):
    print (a-b)
def mul(a,b):
    print (a*b)
def div(a,b):
    print (a/b)
    
while True:
    choice=int(input("select \n-> (1)add\n-> (2)subtract\n-> (3)multiply\n-> (4)divide\n-> Any other number to exit.\n"))
    if(choice<5):
        a=float(input("enter the first number: "))
        b=float(input("enter the second number: "))
        print("the answer is ",end=": ")
    else:
        print("...exiting...")
        break
    match choice:
        case 1:
            add(a,b)
        case 2:
            sub(a,b)
        case 3:
            mul(a,b)
        case 4:
            div(a,b)
