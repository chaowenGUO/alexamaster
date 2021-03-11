import asyncio, pathlib, os

async def f():
    process = await asyncio.create_subprocess_exec('docker', 'run', '--rm', 'python:slim', 'python', '-c', 'import platform; print(platform.python_version())', stdout=asyncio.subprocess.PIPE)
    stdout, _ = await process.communicate()
    print(stdout.decode(), flush=True)
    
asyncio.run(f())
