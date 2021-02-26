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
    if 'websyndic' in driver.current_url: driver.switch_to.window(_)
driver.save_screenshot('a.png')
#while True: pass
driver.quit()
