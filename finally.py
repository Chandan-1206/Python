# finally keyword
def fun():
    try:
        a=[4,6,8,0]
        b=int(input("enter the index : "))
        print(a[b])
        return 0 
    except:
        print("some error occured")
        return 1
    finally: #it is always executed irrespective of return 
        print("it will be always executed")

x=fun()
print(x)
# withoiut funally function will be ended after return without printing 12th line
# used when we want some action to be executed in any condition.
