import {chromium} from 'playwright-chromium'

const browser = await chromium.launch({executablePath:'/usr/bin/google-chrome', args:['--disable-gpu']})//default_args https://github.com/microsoft/playwright/blob/5faf6f9e69c2148e94c81675fb636eb31a02b5e7/src%2Fserver%2Fchromium%2Fchromium.ts#L78
const staroid = await browser.newPage()
await staroid.goto('https://staroid.com/g/chaowenGUOorg/alexamaster/release')
await staroid.click('span:text-is("Sign in with Github")')
await staroid.fill('#login_field', 'chaowen.guo1@gmail.com')
await staroid.screenshot({path:'ha.png'})
await browser.close()
