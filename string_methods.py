# string methods
a="Chandan"
print(a)
print(a.upper())
print(a.lower())
a="!!vanshika!!!"
print(a.rstrip("!"))#only removes after the string 
print(a.replace("vanshika","jaadu"))
b="Nishchay Jaadu Vanisha"
print(b.split(" "))
c="hi My naMe is ChanDan"
print(c.capitalize())
d="Welcome to the console!!!"
print(d.center(50))
print(len(d))
print(len(d.center(50)))
e="hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"
print(e.center(12))# it adds space at the start to get the parameter length to align in center
print(d.count("co"))
print(d.endswith("!!!"))#checks and returns bool value
print(d.endswith("to",4,10))#checks after slicing
print(d.find("co"))
print(d.find("cooo"))
# print(d.index("cooo")) #same as find but gives value error if substring not found instead of -1
e="Vanisha9"
print(e.isalnum())#checks for A-Z,a-z,0-9 
print(e.isalpha())#checks for A-Z,a-z
print(e.islower())
f="Aditya\n"
print(f.isprintable())#checks for chars which are printable only
print(f.isspace())#checks for space given by space bar and tab both
print(f.istitle())#checks if first char of every word is in uppercase and others in lowercase
print(f.isupper())
print(f.startswith("Ad"))#same as endswith but in starting
print(f.swapcase())
g="Hi my name iS deEpak"
print(g.title())
