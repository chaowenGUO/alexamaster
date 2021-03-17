import aiohttp, pathlib, asyncio, sys

async def f():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb') as _:
            pathlib.Path('google-chrome-stable_current_amd64.deb').write_bytes(await _.content.read())
    for _ in await asyncio.gather(asyncio.create_subprocess_exec('apt', 'install', '-y', '--no-install-recommends', './google-chrome-stable_current_amd64.deb'), asyncio.create_subprocess_exec('pip', 'install', 'playwright'), asyncio.create_subprocess_exec('git', 'clone', 'git://github.com/chaowenguoorg/alexamaster')): await _.wait()
    await asyncio.create_subprocess_exec('python', 'alexamaster/py/surf.py')
    await asyncio.sleep(8 * 60 * 60)

asyncio.run(f())
