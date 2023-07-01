# enumerate function

marks1=[58,49,2,8,47,96,91,99,34]
index=0
for m in marks1 :
    if(index==7):
        print(m,end=" ")
        print("topper")
    else:
        print(m)
    index +=1
    
print("\n___________OR by enumerate_________\n")
# OR with the help of enumerate you can directly assign index to a variable like :-
marks2=[58,49,2,8,47,96,91,99,34]
for index,m in enumerate(marks2) :
    if(index==7):
        print(m,end=" ")
        print("topper")
    else:
        print(m)
        
print("\n____________________\n")        
# enumerate creates a tuple originally but by creating two variable tuple is unpacked:-
marks3=[58,49,2,8,47,96,91,99,34]
# to start the function from given index we use start
for tup in enumerate(marks3,start=1) :
    if(tup[0]==8):
        print(tup,end=" ")
        print("topper")
    else:
        print(tup)
print(type(tup))
