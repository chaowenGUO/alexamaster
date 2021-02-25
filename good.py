import selenium.webdriver
options = selenium.webdriver.ChromeOptions()
options.headless = True
options.add_argument('--disable-popup-blocking')
options.add_argument('--incognito')
options.add_argument('--no-first-run')
driver = selenium.webdriver.Chrome(options=options)
driver.execute_script('globalThis.scrollTo(0,document.body.scrollHeight)')
driver.get('https://www.alexamaster.net/sec/login.php')
driver.find_element_by_css_selector('[placeholder="Your Email ..."]').send_keys('chaowen.guo1@gmail.com')
driver.find_element_by_css_selector('[placeholder="Your Password ..."]').send_keys('HL798820y+')
#selenium.webdriver.ActionChains(driver).move_to_element(driver.find_element_by_css_selector('[value="Login Now"]')).click().perform()
driver.save_screenshot('good.png')
driver.close()
