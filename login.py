from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("http://inventory.teamrabbil.com/userLogin",wait_until="networkidle")

    page.locator("#email").fill("test@test.com")
    page.wait_for_timeout(2000)
    page.locator("#password").fill("test123")
    page.wait_for_timeout(2000)

    with page.expect_navigation(wait_until="networkidle"):
        page.get_by_text("Next",exact=False).click()

    browser.close()