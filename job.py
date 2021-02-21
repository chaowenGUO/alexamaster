from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(chrome_options=options)

driver.get('https://www.alexamaster.net/Master/157701')
driver.save_screenshot('screenshot.png')

driver.close()
