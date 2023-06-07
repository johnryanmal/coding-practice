# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

import asyncio

def schedule(f, n):
    async def wrapper():
        await asyncio.sleep(n/1000)
        f()
    asyncio.run(wrapper())

def hello():
    print('hello')

schedule(hello, 1000)

