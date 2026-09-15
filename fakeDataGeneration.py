import csv
import time
import random
from playwright.sync_api import sync_playwright

CSV_PATH = "creds.csv"
REG_URL = "https://inventory.teamrabbil.com/userRegistration"

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


def read_rows(path):
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.reader(f):
            rows.append({
                "email": r[0].strip(),
                "firstname": r[1].strip(),
                "lastname": r[2].strip(),
                "mobile": r[3].strip(),
                "password": r[4].strip(),
            })
    return rows


with sync_playwright() as p:

    rows = read_rows(CSV_PATH)

    browser = p.chromium.launch(
        headless=False,
        # proxy=PROXY
    )

    context = browser.new_context(
        viewport={"width": 1366, "height": 768},
        user_agent=random.choice(USER_AGENTS)
    )

    page = context.new_page()

    for i, r in enumerate(rows, 1):
      
        page.goto(REG_URL, wait_until="networkidle")
        time.sleep(1)

        page.fill("#email", r["email"])
        page.fill("#firstName", r["firstname"])
        page.fill("#lastName", r["lastname"])
        page.fill("#mobile", r["mobile"])
        page.fill("#password", r["password"])

        page.click("text=Complete")

        time.sleep(2)

    context.close()
    browser.close()
