# arbitary funcions
def mavg(*numbers): #numbers becomes a iterable(touple(like an array in c\c++))
    sun=0
    for i in numbers:
        sun=sun+i
    print("the average is :",sun/len(numbers))

mavg(23,69,58,47,12) #any no. of arguments can be placed
