# set methods
s1={1,2,5,6}
s2={3,6,7}
print(s1.union(s2)) #this unites without changing values of s1 and s2
print(s1,s2)
s1.update(s2) #this usnites s2 in s1
print(s1)
s3={8,4,3,6,9,7}
s4={3,2,6,1}
print(s3.intersection(s4)) #does intersection without changing values of s1 and s2
s3.intersection_update(s4) #does intersection of s2 and s1 in s1
print(s3)
s5={7,8,9,5}
s6={2,6,4,1,8,9}
print(s5.symmetric_difference(s6)) # (A union B) - (A intersection B)
s5.symmetric_difference_update(s6)
print(s5)
s7={1,2,3,4,5}
s8={4,5,9,7}
print(s7.difference(s8)) # A-B
s7.difference_update(s8)
print(s7)
s9={2,4,6,8}
s10={3,5,9}
print(s9.isdisjoint(s10)) # check if sets are disjoint(have null intersection)
print(s9.issuperset(s10)) # checks if s9 is superset of s10(s9 already have all elements of s10) 
print(s10.issubset(s9)) # checks if s10 is subset of s9 (opposite of superset)
s10.add(45) # works similar to append in list it adds a new element given to the set
print(s10)
s10.remove(45) #removes the element but gives an error if element is not present in the set
print(s10)
s10.discard(19) #same as remove but doesn't gives an error if element is not present in the set
print(s10)
temp=s9.pop() #it usually removes a last element but as sets are unordered it becomes random
# but we can access the removed element by storing it into a variable
print(s9)
print(temp)
del s9 #deletes the whole set 
s10.clear() #deletes all elements of the set
# print(s9) #will give a name error as now s9 doesn't exists
print(s10)
#to check for an element same as for list
names={"chandan","vanisha","nishchay","jaadu"}
if "vanisha" in names:
    print("yes")
else:
    print("mendak missing")
