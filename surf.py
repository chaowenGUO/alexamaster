import asyncio, playwright.async_api

async def f():
    async with playwright.async_api.async_playwright() as _:
        browser = await _.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--incognito'])#default_args https://github.com/microsoft/playwright/blob/5faf6f9e69c2148e94c81675fb636eb31a02b5e7/src%2Fserver%2Fchromium%2Fchromium.ts#L78
        context = await browser.new_context()
        alexamaster = await context.new_page()
        context.on('page', lambda page: page.bring_to_front())
        await alexamaster.goto('https://www.alexamaster.net/Master/157701')
        crunchingbaseteam = await browser.new_page()
        await crunchingbaseteam.goto('http://www.crunchingbaseteam.com/view.php?user=chaowenguo', timeout=0)
        while True:
            print(len(context.pages), flush=True)
            await asyncio.sleep(60)
            for page in context.pages[1:-1]: await page.close()
asyncio.run(f())
