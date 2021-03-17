import {chromium} from 'playwright-chromium'

const browser = await chromium.launch({executablePath:'/usr/bin/google-chrome', args:['--disable-gpu']})//default_args https://github.com/microsoft/playwright/blob/5faf6f9e69c2148e94c81675fb636eb31a02b5e7/src%2Fserver%2Fchromium%2Fchromium.ts#L78
const colab = await browser.newPage()
await colab.goto('http://www.ebesucher.com/surfbar/chaowenguo')
/*await ebesucher.click('span:text-is("Surf now!")') 
let frame = await ebesucher.waitForSelector('iframe[title="recaptcha challenge"]')
frame = await frame.contentFrame()
await frame.click('#recaptcha-help-button')
await frame.click('#recaptcha-reload-button')
await new globalThis.Promise(_ => globalThis.setTimeout(_, 1000 * 20))
await frame.click('#recaptcha-reload-button')
await frame.click('#recaptcha-help-button')*/
/*await frame.click('.rc-image-title-33:first_of_type')
await frame.click('.rc-image-title-33:nth_of_type(3)')
await frame.click('.rc-image-title-33:last_of_type')
await frame.click('.rc-image-title-33:nth_of_type(5)')*/
/*await frame.click('#recaptcha-audio-button')*/
await new globalThis.Promise(_ => globalThis.setTimeout(_, 1000 * 20))
await ebesucher.screenshot({path:'ha.png'})
await browser.close()
