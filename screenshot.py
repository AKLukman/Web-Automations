from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    # page.goto("https://www.github.com",wait_until="networkidle")

    # screenshot
    # page.screenshot(path="screenshot.png",full_page=True)

    # pdf
    # page.pdf(path="page.pdf",format="A4",print_background=True)

    # set viwport
    # 1920 width and 1080 height: desktop screen
    # 1366 width and 768 height: laptop screen
    # 414 and 896: mobile view
    page.set_viewport_size({"width":1920,"height":1080})
    page.goto("https://www.rabbil.com",wait_until="networkidle")
    page.screenshot(path="screenthot1.png",full_page=True)

    browser.close()
