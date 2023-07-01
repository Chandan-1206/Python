# break and continue
print("break")
for i in range(1,14):
    if(i>10):
        break #comes out of loop
    print("5 x",i,"=",5*i)
print("\ncountinue")
for i in range(1,14):
    if(i==11):
        print("skipped")
        continue # skips the iterator
    print("5 x",i,"=",5*i)
