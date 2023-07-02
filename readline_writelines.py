# readlines,writelines and others

# readline
a=open('proxy2.txt') # file with this name should be present with something written in it
while True:
    line=a.readline()
    print(line)
    if not line:
        print(line,type(line))
        break
a.close()    
# can be used as :-

f=open("proxy.txt") # file with this name should be present and marks like below should be written
# 34,56,98
# 19,16,91
# 33,76,78
i = 0
while True:
    i=i+1
    linee=f.readline()
    if not linee:
        break
# now marks are in string type so to operate on them use type casting 
    m1=int(linee.split(",")[0])
    m2=int(linee.split(",")[1])
    m3=int(linee.split(",")[2])
    print(f"Marks of students {i} in maths is : {m1}")
    print(f"Marks of students {i} in dbms is : {m2}")
    print(f"Marks of students {i} in dsa is : {m3}")
    
    print(linee)

# readlines
b=open("proxy2.txt")
rlines=b.readlines()
print(rlines) # makes a list of lines in the file

# writelines

n=open("jiroz.txt",'w')
wlines= ["once you giveup on your dreams\n","there is nothing to live on\n"] 
# writelines seperates an iterable object like list tuple dictionary into lines and writes them in the file
# and it doesn't adds newlines byitself so \n is to be added by youself or we can use write in loop to write strings seperately
n.writelines(wlines)
n.close()
