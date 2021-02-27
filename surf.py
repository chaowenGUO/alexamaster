import selenium.webdriver, argparse, time, pathlib
parser = argparse.ArgumentParser() 
parser.add_argument('password')
options = selenium.webdriver.ChromeOptions()
options.headless = True
options.add_argument('--disable-popup-blocking')
options.add_argument('--incognito')
options.add_argument('--no-first-run')
driver = selenium.webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get('https://www.alexamaster.net/Master/157701')
driver.execute_script('globalThis.open("https://chrome.google.com/webstore/detail/ebesucher-addon/agchmcconfdfcenopioeilpgjngelefk")')
for _ in driver.window_handles:
    driver.switch_to.window(_)
    if 'ebesucher' in driver.current_url: break
driver.execute_script('globalThis.scrollTo(1000,0)')
time.sleep(10)
#driver.find_element_by_id('connect_button').click()
#driver.find_element_by_id('login_email').send_keys('chaowen.guo1@gmail.com')
#driver.find_element_by_id('login_passwd').send_keys(parser.parse_args().password)
#driver.find_element_by_id('connexion').click()
#driver.find_element_by_id('menu_link_credit').click()
#driver.find_element_by_css_selector('a[onClick^="return visio("]').click()
#while True: pass
driver.save_screenshot('ha.png')
#pathlib.Path('ha.html').write_text(driver.page_source)
driver.quit()
