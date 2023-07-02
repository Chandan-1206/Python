# Snake water gun game (Final) 
import random

score=0
def menu():
    try:
        print("______")
        a=int(input("select:\n1)start\n2)score\n3)exit\n"))
        print("______\n")
        if(a==1):
            func()
        elif(a==2):
            global score
            print(f"\nyour score is : {score}\n")
            menu()
        else:
            print("\nexiting !!!")
            return 0
    except:
        print("invalid choice !!! ")
        menu()
def func():
    cho={'s':'snake','w':'water','g':'gun'}
    comp=random.choice(list(cho.keys()))
    user=input("choose s for snake , w for water and g for gun || m for menu: ")
    try:
        if(user!='s' and user!='w' and user!='g'and user!='m'):
            raise ValueError()
    except Exception:
        print("INVALID input")
        func()
        return 0
    global score
    if(user == comp):
        print("Draw\n")
    elif(user=='s' and comp=='g'):
        print('YOU LOSE !\n')
        score-=1
    elif(user=='w' and comp=='s'):
        score-=1
        print('YOU LOSE !\n')
        score-=1
    elif(user=='g' and comp=='w'):
        print('YOU LOSE !\n')
        score-=1
    elif(user=='m'):
        menu()
        return 0
    else:
        score+=1
        print("you win\n")
    print(f"computer chose: {comp}")
    print(f"you chose: {user}")
    func()
    return 0
menu()

# to learn more about random module:- 
# https://www.w3schools.com/python/module_random.asp
