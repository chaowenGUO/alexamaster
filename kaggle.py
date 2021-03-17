import aiohttp, pathlib, asyncio, sys

async def f():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb') as resp:
            pathlib.Path('google-chrome-stable_current_amd64.deb').write_bytes(await resp.content.read())
    process = await asyncio.create_subprocess_exec('apt', 'install', '-y', '--no-install-recommends', './google-chrome-stable_current_amd64.deb', stdout=asyncio.subprocess.PIPE)
    await asyncio.create_subprocess_exec('pip', 'install', 'playwright')
    await asyncio.create_subprocess_exec('git', 'clone', 'git://github.com/chaowenguoorg/alexamaster')
    #await asyncio.create_subprocess_exec('python', 'alexamaster/py/surf.py')
    #await asyncio.sleep(8 * 60 * 60)
    #sys.exit()
    await asyncio.create_subprocess_exec('apt', 'install', '-y', '--no-install-recommends', './google-chrome-stable_current_amd64.deb')

asyncio.run(f())