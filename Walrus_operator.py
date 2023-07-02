# Walrus operator :=
# it is a new addition to python 3.8 onwards

a=3
print(a:=6) # if we would have used = only then it will give an error

# Without walrus operator:-
'''foods=[] # to make empty list we can also use list()
while True:
    f=input("what food do you like? : ")
    if(f=="quit"):
        break
    else:
        foods.append(f)'''
    
# With walrus operator:-
foods=list()
while((f:=input("what food do you like? : "))!="quit"):
    foods.append(f)
