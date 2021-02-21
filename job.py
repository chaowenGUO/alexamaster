import selenium.webdriver, pathlib
options = selenium.webdriver.ChromeOptions()
options.headless = True
driver = selenium.webdriver.Chrome(chrome_options=options)
driver.implicitly_wait(120)
driver.get('https://www.alexamaster.net/Master/157701')
pathlib.Path('ha.html').write_file(driver.page_source)
driver.close()
