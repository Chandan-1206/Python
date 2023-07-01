# seek,tell and others

# seek()
f=open("zoro.txt",'r')
print(type(f)) # this is just to show that 'read' is in 'io' module 
f.seek(10) # seek function moves the cursor by giver arguments 
print(f.read(5)) # read() reads the file by number arguement 5 means next 5 characters

# tell()
print(f.tell()) # tells the position of the cursor in the file

# truncate()
with open("sanji.txt",'w') as g:
    g.write("hello chandan")
    g.truncate(5) # truncate the file to given size works only in write and append mode
    
with open("sanji.txt",'r') as g:
    print(g.read())
