import random
import time

from playwright.sync_api import sync_playwright


def human_type(element,text):
    for char in text:
        element.type(char,delay=random.randint(300,700)) #key press delay 100ms to 300ms


def human_think(min_sec:0.2,max_sec:1.2):
    time.sleep(random.uniform(min_sec,max_sec))

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("http://inventory.teamrabbil.com/userRegistration",wait_until="networkidle")

    emailInput = page.locator("#email")
    human_think(2,4)
    firstNameInput = page.locator("#firstName")
    human_think(2,4)
    lastNameInput = page.locator("#lastName")
    human_think(2,4)
    mobileInput = page.locator("#mobile")
    human_think(5,10)
    passwordInput = page.locator("#password")


    # human type
    human_type(emailInput,"test20@test.com")
    human_type(firstNameInput,"test20")
    human_type(lastNameInput,"test2020")
    human_type(mobileInput,"01733933859")
    human_type(passwordInput,"test123")

    # page.get_by_text("Complete",exact=False).click()

    time.sleep(10)
    browser.close()