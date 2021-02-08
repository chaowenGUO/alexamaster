import aiohttp, asyncio
    
async def f():
    async with aiohttp.ClientSession() as session: 
        async with session.get('https://v2ex.com/go/jobs') as response: print(await response.text())

asyncio.run(f())
