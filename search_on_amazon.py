import random

from playwright.async_api import async_playwright
import asyncio

KEYWORDS =["laptop","router","pendrive","headphone","heater"]

USER_AGENTS = [
    # Desktop Browsers
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",

    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) "
    "Gecko/20100101 Firefox/123.0",

    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5) AppleWebKit/605.1.15 "
    "(KHTML, like Gecko) Version/16.5 Safari/605.1.15",

    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",

    # Mobile Browsers
    "Mozilla/5.0 (Linux; Android 13; Pixel 6) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36",

    "Mozilla/5.0 (Linux; Android 12; Samsung Galaxy S21) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36",

    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 "
    "(KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",

    "Mozilla/5.0 (Linux; Android 11; Redmi Note 10) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",

    # Tablet
    "Mozilla/5.0 (iPad; CPU OS 16_5 like Mac OS X) AppleWebKit/605.1.15 "
    "(KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",

    "Mozilla/5.0 (Linux; Android 13; SM-T870) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
]

async def search_on_amazon(page,keword):
    await page.goto("https://www.amazon.co.uk",wait_until="domcontentloaded")
    # await page.locator("input[value='Decline']").click() #cookies decline

    box = page.locator("input[role='searchbox']")
    await box.click()
    await box.fill(keword)
    await box.press("Enter")
    await page.wait_for_load_state("domcontentloaded")
    print("Search result found")



async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(user_agent=random.choice(USER_AGENTS))

        # pages
        pages =[]
        for i in range(5):
            eachPage =await context.new_page()
            pages.append(eachPage)

        # tasks
        tasks =[]
        for i in range(5):
            eachTask = search_on_amazon(pages[i],KEYWORDS[i])
            tasks.append(eachTask)


        await asyncio.gather(*tasks)
        await asyncio.sleep(40)
        await browser.close()
        print("done")
        return

asyncio.run(main())