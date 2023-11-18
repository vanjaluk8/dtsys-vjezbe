###### WRITING ASYNC FUNCTIONS
#write an async function that prints "Hello World" and waits for a random itnerval between 1 and 5 second

import asyncio
import random

# async def hello_world():
#     print("Hello World")
#     await asyncio.sleep(random.randint(1,5))
#     print("Hello World")

# asyncio.run(hello_world())

# writing programs using asyncio.cretae_task()
# create two async tasks that are doing simple tasks in the same time
# the first task should print "Hello" every second
# the second task should print "World" every second
# both tasks should run in the same time

async def hello():
    while True:
        print("Hello")
        await asyncio.sleep(5)

async def world():
    while True:
        print("World")
        await asyncio.sleep(1)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(hello())
    loop.create_task(world())
    loop.run_forever()
    loop.close()
    
