# operator overloading

class vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    def __add__(self,x):
        # return f"{self.i+x.i}i + {self.j+x.j}j + {self.k+x.k}k" # if we use this we will get ans as a str 
        # and we wont be able to do further vector operations on it like adding another vector to it 
        return vector(self.i+x.i , self.j+x.j , self.k+x.k) # SO WE USED VECTOR CLASS CONSTRUCTOR
v1=vector(4,3,9)
print(v1)
v2=vector(2,4,8)
print(v2)
# print(v1+v2) # this will give an error without operator overloading (__add__)
# as python doesn't know how to add vector to solve this problem comes operator overloading
# In python operator overloading is done by using dunder methods,there is a different function for different operator
# like __add__ for '+'
# now after using __add__ method for operator overloading we can use + sign to add vectors
print(v1+v2)
print(type(v1+v2))
# to check dunder methods for operator overloading : https://docs.python.org/3/reference/datamodel.html?highlight=__add__
