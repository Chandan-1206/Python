# fstrings

letter="my name is {} and i am from {} "
name="chandan"
country="india"
print(letter.format(name,country))
# or to solve the problem of order we can:
letter1="he my name is {1} and i am from {0} "
print(letter1.format(country,name))
txt="for only {price:.2f} ruppees"
print(txt.format(price=4865.369852147))
# this is the old way we can still use it but in this if we have many variables it becomes confusing
# so after python 3.6 comes fstrings
price=897.365489
text=f"for only {price:.2f} ruppees" #:.2f is like %2f in c and steprecision() in c++
# this is fstring compiler automatically understands by f that {} contains variables
print(text)
# to print fstrings raw we use another {}
age=18
a=f"my age is {age}"
a1=f"my age is {{age}}"
print(a)
print(a1)
