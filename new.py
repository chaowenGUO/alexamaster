import selenium.webdriver, chrome_webstore_download
options = selenium.webdriver.ChromeOptions()
options.headless = True
options.add_argument('--disable-popup-blocking')
options.add_argument('--incognito')
options.add_argument('--no-first-run')
#options.add_argument('--window-size=1960,1080')
driver = selenium.webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get('https://www.alexamaster.net/Master/157701')
driver.execute_script('globalThis.open("http://www.crunchingbaseteam.com/view.php?user=chaowenguo")')
chrome_webstore_download.download('https://chrome.google.com/webstore/detail/ebesucher-addon/agchmcconfdfcenopioeilpgjngelefk', 'ebesucher')
#driver.execute_script('globalThis.open("")')
#for _ in driver.window_handles:
#    driver.switch_to.window(_)
#    if 'ebesucher' in driver.current_url: break
#while True: pass
#driver.save_screenshot('ha.png')
#pathlib.Path('ha.html').write_text(driver.page_source)
driver.quit()