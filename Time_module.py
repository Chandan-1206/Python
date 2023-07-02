# Time module
import time

# time()
def using_while():
    i=0
    while (i<10000):
        i+=1
        print(i)

def using_for():
    for i in range(0,10000):
        print(i)
# time() gives time in sec from 1 jan 1970
fort=time.time()  # time before for loop
using_for()
t1=time.time()-fort # time after for loop - time before for loop gives execution time of for loop
whilet=time.time()
using_while()
t2=time.time()-whilet # same as for loop
print(t1) # printing execution time of for loop
print(t2) #  printing execution time of while loop

# sleep()
print("\nthree")
time.sleep(3) # this delays the time of execution by gives time in seconds 
print("theis is printed after three seconds")

# strftime()
t=time.localtime() # gives local time from the system where the code is executed
formatted_time=time.strftime("%Y/%m/%d  %H:%M:%S",t) # formats time as string
print(formatted_time)
