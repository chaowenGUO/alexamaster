import selenium.webdriver
options = selenium.webdriver.ChromeOptions()
options.headless = True
options.add_argument('--disable-popup-blocking')
options.add_argument('--incognito')
options.add_argument('--no-first-run')
driver = selenium.webdriver.Chrome(options=options)
driver.get('https://www.alexamaster.net/Master/157701')
driver.execute_script('globalThis.open("https://www.websyndic.com")')
for _ in driver.window_handles:
    driver.switch_to.window(_)
    if 'websyndic' in driver.current_url: break
driver.find_element_by_css_selector('')
#while True: pass
driver.quit()
