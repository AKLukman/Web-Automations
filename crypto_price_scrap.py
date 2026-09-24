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


URL ="https://www.coingecko.com/"

async def scroll_full_page(page):
    page_height = await page.evaluate("document.body.scrollHeight")  
    while True:
        await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        await page.wait_for_timeout(5000)
        new_height = await page.evaluate("document.body.scrollHeight")  
        if new_height == page_height:
            break
        page_height = new_height

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
                    user_agent=random.choice(USER_AGENTS),
                    viewport={"width":1200,"height":800},
                    )
        page = await context.new_page()

        await page.goto(URL,wait_until="domcontentloaded")

        await page.wait_for_selector("table tbody tr")

        print("Scrolling...")
        await scroll_full_page(page)

        rows = await page.query_selector_all("table tbody tr")

        result =[]

        for row in rows:
             # Coin Name
            name_element = await row.query_selector("td:nth-child(3) a div div")
            name = (await name_element.text_content()).strip() if name_element else ""

            # Symbol
            symbol_element = await row.query_selector("td:nth-child(3) a div div div")
            symbol = (await symbol_element.text_content()).strip() if symbol_element else ""

            # Price
            price_element = await row.query_selector("td:nth-child(5) span")
            price = (await price_element.text_content()).strip() if price_element else ""

            # 1h %
            h1_element = await row.query_selector("td:nth-child(6) span")
            h1 = (await h1_element.text_content()).strip() if h1_element else ""

            # 24h %
            h24_element = await row.query_selector("td:nth-child(7) span")
            h24 = (await h1_element.text_content()).strip() if h24_element else ""

            # 7d %
            h7d_element = await row.query_selector("td:nth-child(8) span")
            h7d = (await h1_element.text_content()).strip() if h7d_element else ""

            item = {
                "name": name,
                "symbol": symbol,
                "price": price,
                "1h": h1,
                "24h": h24,
                "7d": h7d,
            }

            result.append(item)

        dataFrame = pd.DataFrame(result)
        dataFrame.to_csv("crypto_result.csv",index=False) 


        await page.wait_for_timeout(3000)

        print("Done!")

        await browser.close()


asyncio.run(main())