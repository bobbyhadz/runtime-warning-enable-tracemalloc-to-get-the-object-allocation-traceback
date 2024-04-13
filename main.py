# Enable tracemalloc to get the object allocation traceback

import asyncio


async def greet(name):
    return f'hello {name}'


async def main():
    print(await greet('bobby hadz'))

asyncio.run(main())