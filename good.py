import selenium.webdriver
options = selenium.webdriver.ChromeOptions()
options.headless = True
options.add_argument('--disable-popup-blocking')
options.add_argument('--incognito')
options.add_argument('--no-first-run')
driver = selenium.webdriver.Chrome(options=options)
driver.execute_script('globalThis.scrollTo(0,1000)'）
driver.get('https://www.alexamaster.net/sec/login.php')
driver.find_element_by_css_selector('[placeholder="Your Email ..."]').send_keys('chaowen.guo1@gmail.com')
driver.find_element_by_css_selector('[placeholder="Your Password ..."]').send_keys('HL798820y+')
#driver.find_element_by_css_selector('[value="Login Now"]').click()
driver.save_screenshot('good.png')
driver.close()
