# dictionary methods (almost same as set methods)
ep1={222:69,223:98,224:88,225:79}
ep2={226:48,227:84,228:49}
ep1.update(ep2)
print(ep1)
ep2.clear() 
print(ep2) # gives an empty dictionary
ep3={222:69,223:98,224:81,225:729}
ep3.pop(223) # it removes item by the key
print(ep3)
ep3.popitem() #it removes the item from the last
print(ep3)
del ep1
# print(ep1) #this will give an error as ep1 exists no more
del ep3[222] #this will work as pop()
print(ep3)
# New updates for dictionary methods in python by searching python dictionary documentation
