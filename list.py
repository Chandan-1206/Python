# list
marks=[9,8,7,4,5,63,2,71]
print(marks)
print(type(marks))
print(marks[1]) #like array indexes

l=[2,3,5,6.789,"zoro",True] # can enter element of any datatype in a list 
print(l[-4]) #this is equals to l[len(l)-4] 
print(l[len(l)-4])

#to check for a element in a list:
if '7' in marks:  # 7 exists as an int in the list hence output will be no 
    print("yes")
else:
    print("no")

# can also use index as in range to print elements of a list:
print(l[1:5])
print(l[1:5:2])

# list comprehension:
lst=[i for i in range(10)] # we can use for to make a list from iterables like range
print(lst)
lst2=[i*5 for i in range(10) if i%2==0] # we can use if also 
print(lst2)
