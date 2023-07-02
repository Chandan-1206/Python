# map filter and reduce
def cube(x):
    return x**3
l=[1,2,3,4,5,6,7,8,9]
# to get the cube of the list l :-

# newl=[]
# for i in l:
    # newl.append(cube(i))
# instead we can use map and do the same things easily    
# map
mnewl=list(map(cube,l)) # map gives us a map object so to get a list we have to typecaste it into list
print(mnewl)    
# We can also use lambda and then we won't have to make the cube function :-
mnewl2=list(map(lambda x:x**3,l))
print(mnewl2)

# filter
def filfun(r):
    return r>4
    
fnewl=list(filter(filfun,l)) # filter filters an iterable based on boolean return of a function
print(fnewl)

# here also we can use lambda function inplace of making predicate(function that gives boolean return)
fnewl2=list(filter(lambda r:r>4,l))
print(fnewl2)

# reduce
from functools import reduce # this is important
def mysum(x,y):
    return x+y
ans=reduce(mysum,l) # reduce takes a sequence and applies a function to its element one by one to return a single value
print(ans)
 
# similar to map and filter we can use lambda function
ans2=reduce(lambda x,y:x+y,l)
print(ans2)
