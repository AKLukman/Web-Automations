import random
import time
import pyautogui
from playwright.sync_api import sync_playwright

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


# human like pause
def human_pause(min_sec:0.2,max_sec:1.2):
    time.sleep(random.uniform(min_sec,max_sec))


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page(user_agent=random.choice(USER_AGENTS))
    page.goto("http://inventory.teamrabbil.com/",wait_until="networkidle")

    user_agent = page.evaluate("navigator.userAgent")
    print(user_agent)
    

    # smooth mouse move
    # for i in range(100):
    #     # page.mouse.move(10+i*10,15+i*4)
    #     pyautogui.moveTo(10+i*10,15+i*4)

    #     # small pause
    #     time.sleep(0.01)


    # scroll page down slowly
    for _ in range(45):
        page.mouse.wheel(0,45)
        human_pause(0.02,0.08)


    human_pause(0.5,1.5)

    # scroll page up slowly
    for _ in range(45):
        page.mouse.wheel(0,-45)
        human_pause(0.02,0.08)


    time.sleep(10)

    browser.close()