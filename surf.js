import playwright from 'playwright'

browser = await playwright.chromium.launch({executablePath:'/usr/bin/google-chrome', args:['--disable-gpu']})#default_args https://github.com/microsoft/playwright/blob/5faf6f9e69c2148e94c81675fb636eb31a02b5e7/src%2Fserver%2Fchromium%2Fchromium.ts#L78
context = await browser.newContext()
alexamaster = await context.newPage()
await alexamaster.goto('https://www.alexamaster.net/Master/157701')
crunchingbaseteam = await browser.newPage()
await crunchingbaseteam.goto('http://www.crunchingbaseteam.com/view.php?user=chaowenguo', {timeout:0})
globalThis.setInterval(() => {for (const page of context.pages().slice(1, -1)) await page.close()}, 1800 * 1000)
