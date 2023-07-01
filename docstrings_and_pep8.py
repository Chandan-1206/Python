# docstrings and pep8

# docstrings:
def square(n):
    """takes in a number n and returns its square"""
    print(square._doc_)
    print(n**2)
square(9)    

def add(a,b):
    c=a+b
    '''adds two numbers'''
    print(add._doc_) # this won't work bcz docstring is placed right after function declaration or
                       # are considered as comments
    print(c)
add(8,3)
print("\n\n")

# pep8(python enhancement proposal): is a document that focuses to improve the readability and consistancy
# of the python

# Zen of python (easter egg)
import this
