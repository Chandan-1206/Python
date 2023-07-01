# else with for loop (same as while loop)
for i in range(5):
    print(i)
else:  # THIS ELSE IS EXECUTED WHEN LOOP IS ENDED NOT ON BREAK
    print('ended')

for i in range(7):
    print(i)
    if(i==5):
        break
else: #not printed
    print("ended")
