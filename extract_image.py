import json
import random
from playwright.async_api import async_playwright
import asyncio

from pyautogui import size

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

URL ="https://rabbil.com"

async def main():
        sizes={}
        images=[]

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(user_agent=random.choice(USER_AGENTS))
            page = await context.new_page()

            print("Processing...")

            # Network
            async def add_size(res):
                if res.request.resource_type =="image":
                    body = await res.body()
                    sizes[res.url] = len(body)

            page.on("response",add_size)
            await page.goto(URL,wait_until='load')



            # DOM
            domImages = await page.evaluate("""
            ()=> Array.from(document.images).map(img=>({
                    url:img.src,
                    width: img.naturalWidth,
                    height: img.naturalHeight
                }))
            """)

            # Merge Size KB
            for eachImage in domImages:
                 byte_value=sizes.get(eachImage["url"])
                 eachImage['size_kb']=round((byte_value) / 1024,2)
                 images.append(eachImage)

            # Save The Output
            with open("images.json","w",encoding="utf-8") as f:
                json.dump(images,f,indent=2,ensure_ascii=False)

            print("Done")

            await browser.close()


asyncio.run(main())






