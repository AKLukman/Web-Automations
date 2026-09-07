from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("http://inventory.teamrabbil.com",wait_until="networkidle")

    # text selector
    # element = page.get_by_text("Login")
    # element.click()

    # id selector
    # element = page.locator("#btn")
    # element.click()

    # class selector
    # element = page.glocator(".btn").nth(0)
    # element.click()


    # tag selector
    # element = page.glocator("h2").nth(1)
    # inner_text = element.inner_text()
    # print(inner_text)

    # Read inner html
    # element = page.glocator("form").nth(0)
    # inner_html = element.inner_html()
    # print(inner_html )

    # attribut selector

    nameInputElement = page.locator("input[placeholder='Name']")
    nameInputElement.fill("Lukman")

    page.wait_for_timeout(10000)





    # print("Current page url after click: ",page.url)

    browser.close()