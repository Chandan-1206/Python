#emulating do whie loop
i=100 #even with i>21 loop is executed once just like do while loop (this line was not needed)
while True:
    i=int(input("enter a number: "))
    if(i>21): #stop condition
        break
    print (i)
