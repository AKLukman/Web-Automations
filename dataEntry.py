import csv

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # login
    page.goto("http://inventory.teamrabbil.com/public/userLogin",wait_until="networkidle")

    page.locator("#email").fill("test@test.com")
    page.locator("#password").fill("test123")

    with page.expect_navigation(wait_until="networkidle"):
        page.get_by_text("Next",exact=False).click()

    print("Login done")

    # goto customer page
    page.goto("http://inventory.teamrabbil.com/public/customerPage",wait_until="networkidle")

    # read csv file
    with open("customers.csv",newline="",encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            name = row["customerName"]
            email = row["customerEmail"]
            mobile = row["customerMobile"]

        # open modal
            page.locator("button[data-bs-target='#create-modal']").click()
            page.wait_for_timeout(2000)

            # fill the form
            page.locator("#customerName").fill(name)
            page.locator("#customerEmail").fill(email)
            page.locator("#customerMobile").fill(mobile)

            page.wait_for_timeout(1000)

            # submit form

            page.locator("#save-btn").click()


            page.wait_for_timeout(2000)

            print("Data entry successfull",name)


    browser.close()
