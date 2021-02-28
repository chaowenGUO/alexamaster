import selenium.webdriver, time, threading, pathlib
options = selenium.webdriver.ChromeOptions()
options.headless = True
options.add_argument('--disable-popup-blocking')
options.add_argument('--incognito')
options.add_argument('--no-first-run')
#options.add_extension('agchmcconfdfcenopioeilpgjngelefk_v1.0.28.4.crx')
options.add_argument('--window-size=1024,768')
driver = selenium.webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get('https://www.alexamaster.net/Master/157701')
driver.execute_script('globalThis.open("http://www.crunchingbaseteam.com/view.php?user=chaowenguo")')
driver.execute_script('globalThis.open("http://www.ebesucher.com/surfbar/chaowenguo")')
for _ in driver.window_handles:
    driver.switch_to.window(_)
    if 'ebesucher' in driver.current_url: break
driver.find_element_by_xpath('//*[text()="Surf now!"]/..').click()
time.sleep(10)
pathlib.Path('index.html').write_text(driver.page_source)
#time.sleep(threading.TIMEOUT_MAX)
driver.save_screenshot('ha.png')
driver.quit()
