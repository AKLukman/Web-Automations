from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto("https://rabbil.com",wait_until="networkidle")

    # keyword
    title = page.locator("title").first.inner_text()
    print(title)

    # attribiute

    description = page.locator("meta[name='description']").get_attribute("content")
    print(description)

    browser.close()