import csv
import time
import asyncio
from playwright.async_api import async_playwright

URL="https://inventory.teamrabbil.com/userLogin"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context() # User Agent, Proxy Set
        page = await context.new_page()
        await page.goto(URL,wait_until="load")

        with open("credential.csv",newline="",encoding="utf-8") as csvfile:
                reader=csv.reader(csvfile)
                next(reader,None) # skip header

                for i,row in enumerate(reader):
                    if i>=11:
                        break

                    email=row[0].strip()
                    password = row[1].strip()

                    await page.fill("#email",email)
                    await page.fill("#password", password)

                    try:

                        await page.get_by_text("NEXT").click()
                        await page.wait_for_url("**/dashboard", timeout=5000)
                        print(f"Success -> {i} -> {email}")
                        await context.storage_state(path=f"auth-{i}.json")

                    except Exception:
                            print(f"Fail -> {i}->{email}")


                    await page.goto(URL,wait_until="load")
                    time.sleep(1)


        await browser.close()




asyncio.run(main())













