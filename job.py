import selenium.webdriver

options = selenium.webdriver.ChromeOptions()
options.headless = True
driver = selenium.webdriver.Chrome(chrome_options=options)

driver.get('https://www.alexamaster.net/Master/157701')
driver.save_screenshot('screenshot.png')

driver.close()
