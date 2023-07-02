# Multithreading
import threading
import time 
from concurrent.futures import ThreadPoolExecutor

def func(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)

def main():
    # normal code
    time1=time.perf_counter() # similer to time.time() used to calculate run time of particuar code
    func(3)
    func(2)
    func(1)
    time2=time.perf_counter()
    print("regular time =",time2-time1)
    
    # thread code 
    
    t1= threading.Thread(target=func,args=[3])
    t2= threading.Thread(target=func,args=[2])
    t3= threading.Thread(target=func,args=[1])
    time3=time.perf_counter() 
    t1.start() # this is to start the functions , it will just start the functions 
    t2.start() # and move forward leaving them to execute on their own.
    t3.start()
    time4=time.perf_counter() 
    print("start time for threading =",time4-time3)
    
    t1.join() # this is to wait for every function to be executed before moving forward hence 
    t2.join() # time taken is equals to the time for longest time taking function
    t3.join()
    time5=time.perf_counter()
    print("execution time after using join =",time5-time3)
# main()

# concurrent.futures
def poolingdemo():
  with ThreadPoolExecutor() as executor:
    future1 = executor.submit(func,3)
    future2 = executor.submit(func,2)
    future3 = executor.submit(func,1)
    print(future1.result())
    print(future2.result())
    print(future3.result())
    
# map method
    l=[2,3,5,1]
    results=executor.map(func,l)
    for result in results:
      print(result)
poolingdemo()
