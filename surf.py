import selenium.webdriver, time
options = selenium.webdriver.ChromeOptions()
options.headless = True
options.add_argument('--single-process')
options.add_argument('--disable-popup-blocking')
options.add_argument('--incognito')
options.add_argument('--no-first-run')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
#options.add_argument('--window-size=1960,1080')
driver = selenium.webdriver.Chrome(options=options)
#driver.execute_script('globalThis.open("https://chrome.google.com/webstore/detail/ebesucher-addon/agchmcconfdfcenopioeilpgjngelefk")')
#driver.find_element_by_id('connect_button').click()
#driver.find_element_by_id('login_email').send_keys('c#driver.find_element_by_id('login_passwd').send_keys(parser.parse_args().password)
#driver.find_element_by_id('connexion').click()
#driver.find_element_by_id('menu_link_credit').click()
#driver.find_element_by_css_selector('a[onClick^="return visio("]').click()
driver.get('https://www.alexamaster.net/Master/157701')
driver.execute_script('globalThis.open("http://www.crunchingbaseteam.com/view.php?user=chaowenguo")')
print(len(driver.window_handles))
for _ in driver.window_handles:
    driver.switch_to.window(_)
    print(driver.current_url)
for _ in driver.window_handles:
    driver.switch_to.window(_)
    if 'alexamaster' not in driver.current_url and 'crunchingbaseteam' not in driver.current_url: break
while True:
    time.sleep(60)
    print(len(driver.window_handles))
#driver.save_screenshot('ha.png')
#driver.quit()
