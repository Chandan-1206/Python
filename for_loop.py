# for loop
a=("Chandan")
for i in a: # to print strings as array of characters
    print(i)

colors=["red","yellow","blue","green"] 
for color in colors: # to print elements of a list or other similar iterable objects
    print (color)
    for char in color: # nested for loop 
        print(char)

# range 
           # start stop  step
for i in range(0,   11,    2): # similar to c/c++
    print(i)
