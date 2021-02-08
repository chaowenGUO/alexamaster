import aiohttp
    
async def f():
    async with aiohttp.ClientSession() as session: 
        async with session.post(f'https://api.github.com/repos/chaowenGUOorg/{_}/dispatches') as response: print(await response.text())

asyncio.run(f())
