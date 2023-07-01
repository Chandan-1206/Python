#string slicing and strlen of python 
names="chandan,shivansh"
print(names[0:7])#includes 0 but not 7
print(len(names))
a="mango"
print(a[0:4])
print(a[:4])#python automatically puts 0 at initial position
print(a[1:4])
print(a[2:])#python automatically puts len() at final position
print(a[:-3])#python automatically puts len()before -3
print(a[:len(a)-3])#10th and 11th line works same 
print(a[-1:-3])#it means 4:2 hence no output
print(a[-3:-1])
