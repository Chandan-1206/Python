# File handeling

# Reading a file 

f=open("proxy.txt",'r') # reading mode in text format is default mode while opening a file 
# f=open("proxy.txt") # so this is also in read mode with text format
# f=open("proxy.txt",'rt') # and this is also in read mode with text format(basic syntax)
print(f.read())
f.close() # it is not mandatory but is good practice which shoukd be done to avoid problems

f=open("proxy.txt",'rb') #rb is to open a file in binary format
print(f.read())
f.close()

# creating a file
i=open('jiroz.txt','x') # creates a file and gives an error if file already exists

# writting a file
g=open("proxy2.txt","w") # in writting mode previous data is over written by new one and if file doesn't exists it automatically creates it
g.write("Hi chandan\n") 
g.close() 
# as we are using write mode when we run the program again we won't see 20th line written again as write mode will overwrite previous data
h=open("proxy2.txt",'a') # append mode is similar to write mode but data is appended after previous one instead of overwritting
h.write("everything is working fine ")
h.close()

# with statement
with open("proxy.txt",'a') as f: # 'with' automatically closes the file after you are done with it
    f.write("its easy ,right?")
