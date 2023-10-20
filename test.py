import asyncio
from time import sleep


async def masala():
    print('Maslani yechyapman')
    await asyncio.sleep(0.1)


async def main():
    tasks = []
    for i in range(10_000):
        task = asyncio.create_task(masala())
        tasks.append(task)
        print(i)
    asyncio.gather(*tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())