from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page();

    # signup page
    page.goto("http://inventory.teamrabbil.com/userRegistration",wait_until="networkidle")

    # form fill up
    emailInputElements = page.locator("#email").fill("test@test.com")
    emailInputElements = page.locator("#firstName").fill("test")
    emailInputElements = page.locator("#lastName").fill("test2")
    emailInputElements = page.locator("#mobile").fill("37878363355")
    emailInputElements = page.locator("#password").fill("test123")

    # smart waiting
    with page.expect_navigation(wait_until="networkidle"):
        page.get_by_text("Complete").click()


    print("Singup successfull.")
    print(page.url)
    browser.close()

