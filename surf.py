import asyncio, playwright.async_api, itertools

async def f():
    async with playwright.async_api.async_playwright() as _:
        browser = await _.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--disable-gpu'])#default_args https://github.com/microsoft/playwright/blob/5faf6f9e69c2148e94c81675fb636eb31a02b5e7/src%2Fserver%2Fchromium%2Fchromium.ts#L78
        context = await browser.new_context()
        alexamaster = await context.new_page()
        await alexamaster.goto('https://www.alexamaster.net/Master/157701')
        crunchingbaseteam = await browser.new_page()
        await crunchingbaseteam.goto('http://www.crunchingbaseteam.com/view.php?user=chaowenguo', timeout=0)
        while True:
            await asyncio.sleep(300)
            for page in itertools.islice(context.pages, 1, len(context.pages) - 1): await page.close()

asyncio.run(f())
