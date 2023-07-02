# List methods
l=[11,45,1,2,4,6]
print(l)
l.append(7) #adds new element to thew list at the end
print(l) 
l.sort() #sorts the list in ascending order
print(l) 
l.sort(reverse=True) #sorts the list in descending order
print(l)
a=[29,65,24,65,2]
a.reverse() #it reverses the array
print(a)
b=[47,69,67,2,14,2,36]
print(b.index(2)) #gives the index of the element 
print(b.count(2)) #count the no. of time an element is present in the list
# c=b #if we do this and then change c it also changes b in python bcz it acts as a reference
# c[0]=0
# print(b) 
# so to avoid this we use copy 
c=b.copy() #makes a copy of the list
c[0]=3
print(b)
b.insert(2,68) #used to insert an element at a particular index like in stl c++
print(b)
d=[1,2,3,4,5,6,7]
e=[80,90,100]
d.extend(e) #this extends list d and adds elements of e at the end
print(d)
#but this will change list d if you want to concatinate two lists you can use:
d=[1,2,3,4,5,6,7]
e=[80,90,100]
f=d+e #for concatination of e in d
g=e+d #for concatination of d on e
print(f)
print(g)
