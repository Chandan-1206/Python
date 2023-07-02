# AsyncIO
import asyncio
import time 

def fun1():
    time.sleep(3)
    print("fun 1")
def fun2():
    time.sleep(3)
    print("fun 2")
def fun3():
    time.sleep(3)
    print("fun 3")
    
fun1()
fun2()
fun3()
# In above code one by one function will be executed to execute them concurrently we use async
async def function1(): # async keywords to make the function asynchronous
    await asyncio.sleep(3) # await suspends execution until others are in processing
    print("function 1")
async def function2():
    await asyncio.sleep(3)
    print("function 2")
async def function3():
    await asyncio.sleep(3) 
    print("function 3")

async def main():    
    L=await asyncio.gather( # used for parallel execution .also prints return value in a list.
    function1(),
    function2(),
    function3()
    )
    print(L)
asyncio.run(main()) # to run main function 

# request module can be used to download imgs using url to see the practical use of asyncio
