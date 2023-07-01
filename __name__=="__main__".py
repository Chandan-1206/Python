# if __name__=="__main__" 
# chandan.py - file 1
def hi():
    print("you are welcome my frnd")
# hi()    

# now if we will import this program into another program hi will be executed from this program on importing 
# this makes it a big problem when dealing with critical functions like function deleting all files
# so to solve this problem we use if __name__=="__main__" like:-
if __name__=="__main__":
    hi()
# this will check if the program is being run from original one or is being imported if is imported then 
# if statement won't be executed 


# if __name__=="__main__" 
# main.py - file 2
import chandan as me
me.hi()
# when we will run hi() will be executed twice once from chandan.py when importing and then here 
# to solve this we have used if __name__=="__main__" in impoerted file
