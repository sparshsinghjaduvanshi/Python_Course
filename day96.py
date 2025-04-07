#Async IO in Python

'''asynchronous I/O ,or async for shot,is a programming pattern that allows for high-
    performance I/O operations in a concurrent and nn-blocking manner In Python,
    async programming is achieved through the use of the asyncio mofdule and asynchronous functions.'''

'''Syntax :- '''

import asyncio
import time

async def function1():
    await asyncio.sleep(2)
    print("funct1")

async def function2():
    await asyncio.sleep(2)
    print("funct2")

async def function3():
    await asyncio.sleep(3)
    print("funct3")

async def main():
    # tast = asyncio.create_task(function1())
    # await function2()
    # await function3()

    l = await asyncio.gather(
         function1(),
         function2(),
         function3()     )
    print(l)

asyncio.run(main())