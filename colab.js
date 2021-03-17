import {chromium} from 'playwright-chromium'

const browser = await chromium.launch({executablePath:'/usr/bin/google-chrome', args:['--disable-gpu']})//default_args https://github.com/microsoft/playwright/blob/5faf6f9e69c2148e94c81675fb636eb31a02b5e7/src%2Fserver%2Fchromium%2Fchromium.ts#L78
const context = await browser.newContext()
for (const _ of Array(5).keys())
{
    const page = await context.newPage()
    await page.goto(['https://colab.research.google.com/github/chaowenGUOorg/alexamaster/blob/main/colab', _, '.ipynb'].join(''))
    await page.keyboard.press('Control+F9')
}
await browser.close()
