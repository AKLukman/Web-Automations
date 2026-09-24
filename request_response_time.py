import json
import random
import time
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



URL = "https://www.rabbil.com"

def is_api(url):
    clean = url.split("?", 1)[0]
    clean = clean.split("#", 1)[0]
    clean_no_slash = clean.rstrip("/")
    last = clean_no_slash.rsplit("/", 1)[-1]
    return "." not in last


async def main():

    api_logs =[]
    start_times={}


    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(user_agent=random.choice(USER_AGENTS))
        page = await context.new_page()

        # Request Event
        async def on_request(req):
            if is_api(req.url):
                start_times[req]=time.perf_counter()
                # {req:400,}

        #Response Event
        async def on_response(res):
            if is_api(res.url):
                req= res.request
                url = req.url
                method=req.method
                status=res.status

                start = start_times.pop(req,None)
                end= time.perf_counter()
                duration_ms = round((end-start)*1000,2) if start else 0

                try:
                    req_body= await req.post_data()
                except:
                    req_body=None

                try:
                    res_body= await res.json()
                except:
                    res_body=None

                api_logs.append({
                    "url": url,
                    'duration_ms':duration_ms,
                    "method": method,
                    "status": status,
                    "req_body": req_body,
                    "res_body": res_body
                })



        page.on("request", on_request)
        page.on("response", on_response)

        await page.goto(URL, wait_until="load")


        with open('api_logs.json', 'w',encoding='utf-8') as file:
            json.dump(api_logs, file, ensure_ascii=False, indent=4)



        print("Done")
        await browser.close()


asyncio.run(main())
