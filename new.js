/*import selenium.webdriver, selenium.webdriver.support.expected_conditions, time, threading, pathlib
options = selenium.webdriver.ChromeOptions()
options.headless = True
options.add_argument('--disable-popup-blocking')
options.add_argument('--incognito')
options.add_argument('--no-first-run')
#options.add_extension('agchmcconfdfcenopioeilpgjngelefk_v1.0.28.4.crx')
options.add_argument('--window-size=1024,768')
driver = selenium.webdriver.Chrome(options=options)
driver.get('https://www.alexamaster.net/Master/157701')
driver.execute_script('globalThis.open("http://www.crunchingbaseteam.com/view.php?user=chaowenguo")')
driver.execute_script('globalThis.open("http://www.ebesucher.com/surfbar/chaowenguo")')
for _ in driver.window_handles:
    driver.switch_to.window(_)
    if 'ebesucher' in driver.current_url: break
selenium.webdriver.support.ui.WebDriverWait(driver, 10).until(selenium.webdriver.support.expected_conditions.element_to_be_clickable((selenium.webdriver.common.by.By.XPATH, '//*[text()="Surf now!"]/..'))).click()
selenium.webdriver.support.ui.WebDriverWait(driver, 10).until(selenium.webdriver.support.expected_conditions.frame_to_be_available_and_switch_to_it((selenium.webdriver.common.by.By.CSS_SELECTOR, 'iframe[title="recaptcha challenge"]')))
selenium.webdriver.support.ui.WebDriverWait(driver, 10).until(selenium.webdriver.support.expected_conditions.element_to_be_clickable((selenium.webdriver.common.by.By.ID, 'recaptcha-audio-button'))).click()
#time.sleep(threading.TIMEOUT_MAX)
time.sleep(20)
pathlib.Path('index.html').write_text(driver.execute_script("return document.documentElement.outerHTML"))
driver.save_screenshot('ha.png')
driver.quit()*/

import {chromium} from 'playwright-chromium'

const browser = await chromium.launch({executablePath:'/usr/bin/google-chrome', args:['--disable-gpu']})//default_args https://github.com/microsoft/playwright/blob/5faf6f9e69c2148e94c81675fb636eb31a02b5e7/src%2Fserver%2Fchromium%2Fchromium.ts#L78
const ebesucher = await browser.newPage()
await ebesucher.goto('http://www.ebesucher.com/surfbar/chaowenguo')
await ebesucher.click('"Surf now!"')
let frame = await ebesucher.$('iframe[title="recaptcha challenge"]')
frame = await frame.contentFrame()
frame.click('#recaptcha-audio-button')
await ebesucher.screenshot({path:'ha.png'})
await browser.close()
