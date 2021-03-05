import asyncio, playwright.async_api

async def f():
    async with playwright.async_api.async_playwright() as _:
        browser = await _.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--incognito'])#default_args https://github.com/microsoft/playwright/blob/5faf6f9e69c2148e94c81675fb636eb31a02b5e7/src%2Fserver%2Fchromium%2Fchromium.ts#L78
        context = await browser.new_context()
        alexamaster = await context.new_page()
        context.on('page', lambda page: page.bring_to_front())
        await alexamaster.goto('https://www.alexamaster.net/Master/157701')
        crunchingbaseteam = await browser.new_page()
        await crunchingbaseteam.goto('http://www.crunchingbaseteam.com/view.php?user=chaowenguo', timeout=0)
        while True:
            print(len(context.pages), flush=True)
            await asyncio.sleep(60)
            for page in context.pages()[1:-1]: page.close()
asyncio.run(f())

#options.add_argument('--incognito')
#options.add_argument('--window-size=1960,1080')
#driver = selenium.webdriver.Chrome(options=options)
#driver.execute_script('globalThis.open("https://chrome.google.com/webstore/detail/ebesucher-addon/agchmcconfdfcenopioeilpgjngelefk")')
#driver.find_element_by_id('connect_button').click()
#driver.find_element_by_id('login_email').send_keys('c#driver.find_element_by_id('login_passwd').send_keys(parser.parse_args().password)
#driver.find_element_by_id('connexion').click()
#driver.find_element_by_id('menu_link_credit').click()
#driver.find_element_by_css_selector('a[onClick^="return visio("]').click()
#driver.get('https://www.alexamaster.net/Master/157701')
#driver.execute_script('globalThis.open("http://www.crunchingbaseteam.com/view.php?user=chaowenguo")')
#while True:
#    time.sleep(3 * 60 * 60)
#    for _ in itertools.islice(driver.window_handles, 2, None):
#        driver.switch_to.window(_)
#        driver.close()
#    driver.switch_to.window(driver.window_handles[0])
#    time.sleep(60)
#    driver.refresh()
#driver.save_screenshot('ha.png')
#driver.quit()
