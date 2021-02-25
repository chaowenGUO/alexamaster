import selenium.webdriver, time, PIL, io, asyncio, aiohttp
async def f():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://www.alexamaster.net/sec/login.php') as response:
            with io.BytesIO(await response.content.read()) as _:               
asyncio.run(f())

options = selenium.webdriver.ChromeOptions()
options.headless = True
options.add_argument('--disable-popup-blocking')
options.add_argument('--incognito')
options.add_argument('--no-first-run')
driver = selenium.webdriver.Chrome(options=options)
driver.get('https://www.alexamaster.net/sec/login.php')
driver.execute_script('globalThis.scrollTo(0,1000)')
time.sleep(10)
driver.find_element_by_css_selector('[placeholder="Your Email ..."]').send_keys('chaowen.guo1@gmail.com')
driver.find_element_by_css_selector('[placeholder="Your Password ..."]').send_keys('HL798820y+')
driver.find_element_by_css_selector('[value="Login Now"]').click()
time.sleep(60)
driver.save_screenshot('good.png')
driver.close()
