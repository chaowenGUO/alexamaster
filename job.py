import cloudscraper

scraper = cloudscraper.create_scraper()
print(scraper.get('https://v2ex.com/go/jobs').text)

import aiohttp, asyncio, bs4
    
async def f():
    async with aiohttp.ClientSession() as session:
        for _ in range(1, 2): 
            async with session.get(f'https://v2ex.com/go/jobs?p={_}') as response: 
                #soup = bs4.BeautifulSoup(await response.text())
                #print(soup.select('.item_title'))
                print(await response.text())
        #async with session.get(f'https://v2ex.com/go/jobs?p=150') as response: 
            #print(await response.text())

asyncio.run(f())
