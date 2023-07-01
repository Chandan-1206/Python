# operations on tuples
# we can't change tuple directly so in order to change it we must change it into a list first and 
# then after changing convert it back to tuple  
countries=("india","russia","usa","canada","nepal")
print(countries)
temp=list(countries)
temp.append("australia")
temp.pop(2)
temp.insert(2,"japan")
countries=tuple(temp)
print(countries)

a=(2,3,4,6,8,9,2,4,1,6,8,6,0,3,3,4,7,1)
print(a.index(3))    #if the value in not present in the touple it will raise a value error
res=a.index(3,4,16)  #this will slice the touple from index 4 to 16 and then check the index of 3 in it 
print(res)
print(a.count(8)) 
print(len(a))
b=(7,19,4,1)
c=a+b # use to concatinate b in a
d=b+a # use to concatinate a in b
print(c)
print(d)
