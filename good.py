import selenium.webdriver, time, PIL, io, pytesseract
#async def f():
#    async with aiohttp.ClientSession() as session:
#        async with session.get('https://www.alexamaster.net/sec/image.php') as response:
#            a = PIL.Image.open(io.BytesIO(await response.content.read()))
#            a = a.convert('L')  # 处理灰度
#            a = a.point(lambda _:255 if _ > 150 else 0)
#            a.save('ocr.png')
#            return pytesseract.image_to_string(a)   

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
driver.find_element_by_css_selector('input[value="Login Now"]').click()
time.sleep(60)
good = PIL.Image(io.BytesIO(driver.get_screenshot_as_png()))
ocr = driver.find_element_by_css_selector('img[src=image.php]')
ocr = good.crop((ocr.location['x'], ocr.location['y'], ocr.location['x'] + ocr.size['width'], ocr.location['y'] + ocr.size['height']))
a.save('good.png')
ocr.save('ocr.png')
driver.close()
