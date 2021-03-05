import asyncio, playwright.async_api, itertools

async def f():
    print(1, flush=True)
    async with playwright.async_api.async_playwright() as _:
        browser = await _.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--incognito'])#default_args https://github.com/microsoft/playwright/blob/5faf6f9e69c2148e94c81675fb636eb31a02b5e7/src%2Fserver%2Fchromium%2Fchromium.ts#L78
        print(2, flush=True)
        context = await browser.new_context()
        print(3, flush=True)
        context.on('page', lambda page: page.bring_to_front())
        print(4, flush=True)
        alexamaster = await context.new_page()
        print(5, flush=True)
        await alexamaster.goto('https://www.alexamaster.net/Master/157701')
        print(6, flush=True)
        crunchingbaseteam = await browser.new_page()
        print(7, flush=True)
        await crunchingbaseteam.goto('http://www.crunchingbaseteam.com/view.php?user=chaowenguo', timeout=0)
        print(8, flush=True)
        while True:
            print(len(context.pages), flush=True)
            await asyncio.sleep(60)
            for page in itertools.islice(context.pages, 1, len(context.pages) - 1): await page.close()
asyncio.run(f()
