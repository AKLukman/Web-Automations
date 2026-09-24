import asyncio
import random

import pandas as pd

from playwright.async_api import async_playwright
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

URL ="https://www.bbc.co.uk/"
async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
            user_agent=random.choice(USER_AGENTS),
            viewport={"width":1200,"height":800},
            locale="en_uk"
            )
        page = await context.new_page()


        await page.goto(URL,wait_until="domcontentloaded")
        await page.wait_for_selector("span[aria-hidden='false']",timeout=3000)

        await page.wait_for_timeout(3000)
        items = await page.query_selector_all("span[aria-hidden='false']")

        data =[]

        for i,item in enumerate(items[:20]):
            title = (await item.text_content()).strip()
            data.append({"id":i,"title":title})

        dataFrame = pd.DataFrame(data)
        dataFrame.to_csv("bbc.csv",index=False,encoding="utf-8")

        print("done")
        await browser.close()

asyncio.run(main())