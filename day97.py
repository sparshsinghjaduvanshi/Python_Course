#MULTITHREADIG

'''it is a tehnique that allows multiple threads of execution to run
    concurrently within a single proces.In Pytho ,we can use the hreading module 
    to implement multithreading .'''

'''import threading'''
#CREATING A THREAD
'''to create a thread ,we need to create a Thread object and then call its stat() method.
    The start() method runs the thread and then to stop the execution, we use the join()
    method .Here's how we can create a simple thread.
    
    
    import threading
    def my_func():
        pritn("Hello from thread",threding.current_Thread().name)
        thread = threading.Thread(target=my_func)
        thread.start()
        thread.join()''' 

import threading
import time

#Indecates some task being done
def func(sec):
    print(f"Sleeping for {sec} seconds.")
    time.sleep(sec)

time1 = time.perf_counter()
#Normal code
# func(4)
# func(2)
# func(1)

#Code using thread
t1 = threading.Thread(target=func, args=[4])#target means the targeted function,args means the argument we need to pass to the function.
t2 = threading.Thread(target=func, args=[2])
t3 = threading.Thread(target=func, args=[1])

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

time2 = time.perf_counter()
print(time2 - time1)