import aiohttp, asyncio
    
async def f():
    async with aiohttp.ClientSession() as session:
        for _ in range(1, 1000): async with session.get(f'https://v2ex.com/go/jobs?p=') as response: print(await response.text())

asyncio.run(f())
