# match case (only available in python 3.10 and later )
a=int(input("enter the value : "))
match a:
    case 1:
        print("one")
    case 2:
        print("two")
    case _ if(a>50):  #we can use if else in default case also
        print("value too big")
    case _:
        print("more than two")
