# shadode Module - self made module for mostly used logics

# prime check
def prime(n):
    count=0
    for i in range(2,n):
        if(n%i==0):
            count+=1
    
    if(count==0):
        print("it is a prime number")
        return True
    else:
        print("it is not a prime number")
        return False

#prime numbers till n
def allprime(n):
    for j in range(2,n):
        count=0
        for i in range(2,j):
            if(j%i==0):
                count+=1
        if(count==0):
            print(j,end="\t")
    print("\n",end="")
