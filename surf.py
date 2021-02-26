import selenium.webdriver, time
options = selenium.webdriver.ChromeOptions()
options.headless = True
options.add_argument('--disable-popup-blocking')
options.add_argument('--incognito')
options.add_argument('--no-first-run')
driver = selenium.webdriver.Chrome(options=options)
driver.get('https://www.alexamaster.net/Master/157701')
driver.execute_script('globalThis.open("https://www.websyndic.com")')
#driver.switch_to_window(driver.window_handles[-1])
#driver.save_screenshot('eb.png')
time.sleep(120)
for _ in driver.window_handles:
    driver.switch_to_window(_)
    driver.save_screenshot(driver.title + '.png')
#while True: pass
driver.quit()
