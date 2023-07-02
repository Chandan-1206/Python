# generators
import time # just to check time difference for generators and normal iterators 
def my_gen():
    for i in range(1000):
        yield i+1 # this makes the function a generator 

g=my_gen()
print(next(g)) # next is used to execute generator for next value
print(next(g))
print(next(g))
print(next(g))
# to print in a sequence 
t=time.time()
for j in g:
    print(j)
gentime=time.time()-t

def norm():
    for i in range(1000):
        return i+1
        

t2=time.time()
print(norm())
normtime=time.time()-t2
print(f"time taken by norm is {normtime}")
print(f"time taken by my_gen is {gentime}")
