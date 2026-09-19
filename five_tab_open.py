import random

from playwright.async_api import async_playwright
import asyncio

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
async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False);
        context = await browser.new_context(user_agent=random.choice(USER_AGENTS))

        urls =[
            "https://www.amazon.co.uk",
            "https://github.com/",
            "https://inventory.teamrabbil.com",
            "https://www.youtube.com",
            "https://www.bing.com"
        ]

        # pages create
        pages =[]

        for i in range(5):
            eachPage = await context.new_page()
            pages.append(eachPage)

        # tasks
        tasks =[]
        for i in range(5):
            eachTask = pages[i].goto(urls[i])
            tasks.append(eachTask)

        await asyncio.gather(*tasks)
        print("done")
        await asyncio.sleep(15)
        await browser.close()



asyncio.run(main())