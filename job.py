import selenium.webdriver, time
options = selenium.webdriver.ChromeOptions()
options.headless = True
options.add_argument('--disable-popup-blocking')
driver = selenium.webdriver.Chrome(chrome_options=options)
driver.get('https://www.alexamaster.net/Master/157701')
time.sleep(21600)
#driver.close()
