# clock and if else statements
import time
t=time.strftime('%H:%M:%S')
print(t)
h=int(time.strftime("%H"))
if (h<12):
    print("good morning")
elif(h<15):
    print("good afternoon")
elif(h<19):
    print("good evening")
else:
    print("good night")
