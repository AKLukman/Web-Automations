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


async def get_meta(page, selector, attr="content"):
    el = await page.query_selector(selector)
    return await el.get_attribute(attr) if el else ""



async def main():
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        await page.goto(url, wait_until="domcontentloaded")
        await page.wait_for_timeout(5000)

        video_id = url.split("v=")[-1]

        data = {
            "video_url": url,
            "video_id": video_id,

            # SEO / Meta
            "title": await get_meta(page, 'meta[name="title"]'),
            "description": await get_meta(page, 'meta[name="description"]'),
            "keywords": await get_meta(page, 'meta[name="keywords"]'),
            "og_title": await get_meta(page, 'meta[property="og:title"]'),
            "og_description": await get_meta(page, 'meta[property="og:description"]'),
            "og_tags": await get_meta(page, 'meta[property="og:video:tag"]'),

            # Thumbnails
            "thumbnail_default": f"https://img.youtube.com/vi/{video_id}/default.jpg",
            "thumbnail_medium": f"https://img.youtube.com/vi/{video_id}/mqdefault.jpg",
            "thumbnail_high": f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg",
            "thumbnail_max": f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg",

            # Channel Info
            "channel_name": await page.locator("ytd-channel-name a").inner_text(),
            "channel_url": await page.locator("ytd-channel-name a").get_attribute("href"),
        }

        await browser.close()

    # Save CSV
    df = pd.DataFrame([data])
    df.to_csv("youtube_full_seo.csv", index=False, encoding="utf-8")

    print("youtube_full_seo.csv saved successfully")
    print(data)


asyncio.run(main())




  
