import random
import time

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


PROXIES=[
    {
        "server":"http://dc.decodo.com:10001",
        "username":'spofsbf6ub',
        "password":"9zMcvDnc6wfs58CxI+"
    },
    {
        "server":"http://dc.decodo.com:10002",
        "username":'spofsbf6ub',
        "password":"9zMcvDnc6wfs58CxI+"
    },
    {
        "server":"http://dc.decodo.com:10003",
        "username":'spofsbf6ub',
        "password":"9zMcvDnc6wfs58CxI+"
    },
    {
        "server":"http://dc.decodo.com:10004",
        "username":'spofsbf6ub',
        "password":"9zMcvDnc6wfs58CxI+"
    },
    {
        "server":"http://dc.decodo.com:10005",
        "username":'spofsbf6ub',
        "password":"9zMcvDnc6wfs58CxI+"
    },
    {
        "server":"http://dc.decodo.com:10006",
        "username":'spofsbf6ub',
        "password":"9zMcvDnc6wfs58CxI+"
    },

]

SESSION=10
TARGET_URL="http://inventory.teamrabbil.com"


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    for _ in range(SESSION):
        context = browser.new_context(user_agent=random.choice(USER_AGENTS),proxy=random.choice(PROXIES))
        page = context.new_page()

        page.goto(TARGET_URL,wait_until="networkidle")
        time.sleep(random.uniform(1,3))


        for _ in range(4):
            page.evaluate("window.scrollBy(0,500)")
            time.sleep(random.uniform(0.5,1.2))


        time.sleep(random.uniform(2,4))

        context.close()

        time.sleep(random.uniform(2,4))

    browser.close()

        