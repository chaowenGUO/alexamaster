import selenium.webdriver, selenium.webdriver.support.expected_conditions, time, threading, pathlib
options = selenium.webdriver.ChromeOptions()
options.headless = True
options.add_argument('--disable-popup-blocking')
options.add_argument('--incognito')
options.add_argument('--no-first-run')
#options.add_extension('agchmcconfdfcenopioeilpgjngelefk_v1.0.28.4.crx')
options.add_argument('--window-size=1024,768')
driver = selenium.webdriver.Chrome(options=options)
driver.get('https://www.alexamaster.net/Master/157701')
driver.execute_script('globalThis.open("http://www.crunchingbaseteam.com/view.php?user=chaowenguo")')
driver.execute_script('globalThis.open("http://www.ebesucher.com/surfbar/chaowenguo")')
for _ in driver.window_handles:
    driver.switch_to.window(_)
    if 'ebesucher' in driver.current_url: break
selenium.webdriver.support.ui.WebDriverWait(driver, 10).until(selenium.webdriver.support.expected_conditions.element_to_be_clickable((selenium.webdriver.common.by.By.XPATH, '//*[text()="Surf now!"]/..'))).click()
selenium.webdriver.support.ui.WebDriverWait(driver, 10).until(selenium.webdriver.support.expected_conditions.frame_to_be_available_and_switch_to_it((selenium.webdriver.common.by.By.CSS_SELECTOR, 'iframe[title="recaptcha challenge"]')))
selenium.webdriver.support.ui.WebDriverWait(driver, 10).until(selenium.webdriver.support.expected_conditions.element_to_be_clickable((selenium.webdriver.common.by.By.Id, 'recaptcha-audio-button'))).click()
#time.sleep(threading.TIMEOUT_MAX)
time.sleep(20)
pathlib.Path('index.html').write_text(driver.execute_script("return document.documentElement.outerHTML"))
driver.save_screenshot('ha.png')
driver.quit()
