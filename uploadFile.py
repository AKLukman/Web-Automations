import os
import time

from playwright.sync_api import sync_playwright

# http://inventory.teamrabbil.com/public/UploadPage
# http://inventory.teamrabbil.com/public/DownloadPage

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("http://inventory.teamrabbil.com/public/UploadPage",wait_until="networkidle")

    for fileName in os.listdir("images"):
        filePath = os.path.join("images",fileName)

        # file set on input type
        page.set_input_files("input[name='file']",filePath)
        page.click("button[type='submit']")

        # check upload
        try:
            page.wait_for_selector(".alert-success",timeout=5000)
            print(f"{fileName} is uploaded")

        except:
            print(f"{fileName} is upload failed.")

# small delay
        time.sleep(5) 
# page reload for prepare next upload
        page.reload(wait_until="networkidle")

    browser.close()

