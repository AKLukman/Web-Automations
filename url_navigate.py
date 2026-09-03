from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page();

    # page browse
    page.goto("https://www.google.com/")
    page.wait_for_timeout(5000)

    # new page browse
    page.goto("https://www.github.com")
    page.wait_for_timeout(5000)

    # new page browse
    page.goto("https://www.rabbil.com")
    page.wait_for_timeout(5000)

    # page reload
    page.reload()
    page.wait_for_timeout(5000)

    # page go back
    page.go_back()
    page.wait_for_timeout(5000)

    # page forward
    page.go_forward()
    page.wait_for_timeout(5000)

    browser.close()

   
