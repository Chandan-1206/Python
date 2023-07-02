# 'is' vs '=='

a=[4,2,4,5,1]
b=[4,2,4,5,1]
print(a is b) # compares the locataion
print(a==b,'\n') # compares the value
x=y=[15,16]
# now y will have same location and positon as x
print(x is y)
print(x == y,'\n')
c=34
d=34
print(c is d)
print(c==d,'\n')
# for immutable objects like int string touple etc ,pyhton points variable having same value to same location
