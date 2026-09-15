from playwright.sync_api import sync_playwright
import random
import time

TARGET = "https://www.youtube.com/watch?v=xAPJoQ8EiSQ"
SESSIONS = 2

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/121 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 Chrome/121 Mobile Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5) AppleWebKit/605.1.15 Version/16.4 Safari/605.1.15",
]

PROXY = {
    "server": "http://gate.decodo.com:10003",
    "username": "sp8tcdlo12",
    "password": "a3+yfO2WjCesfh5O7l"
}

with sync_playwright() as p:

    for i in range(SESSIONS):
        print(f" Session {i+1}/{SESSIONS}")

        try:
            browser = p.chromium.launch(
                headless=False,
                proxy=PROXY   # ← added here
            )

            context = browser.new_context(
                user_agent=random.choice(USER_AGENTS),
                viewport={"width": 1366, "height": 768},
            )

            page = context.new_page()

            page.goto(TARGET, wait_until="domcontentloaded", timeout=45000)
            time.sleep(random.uniform(1, 2))

            # Try play button (optional)
            button = page.locator("button[aria-label='Play']")
            if button.count() > 0:
                button.click()

            print("Watching 10 sec...")
            time.sleep(10)

        except Exception as e:
            print("Error:", e)

        print("Closing browser")
        context.close()
        browser.close()

        time.sleep(random.uniform(1, 3))
