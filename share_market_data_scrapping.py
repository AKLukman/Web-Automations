import asyncio
from playwright.async_api import async_playwright
import pandas as pd

async def main():

    url="https://www.dsebd.org/latest_share_price_scroll_by_volume.php"

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto(url)
        # Wait Until Table Appear
        await page.wait_for_selector("table.shares-table tbody tr")

        # Select All Rows
        all_rows = await page.query_selector_all("table.shares-table tbody tr")

        result=[]

        for each_row in all_rows:
            all_columns = await each_row.query_selector_all("td")

            values = []
            for each_column in all_columns:
                text = await each_column.text_content()
                values.append(text)

            print(values[0])

            item={
                "SL": values[0],
                "TRADING_CODE": values[1],
                "LTP": values[2],
                "HIGH": values[3],
                "LOW": values[4],
                "CLOSEP": values[5],
                "YCP": values[6],
                "CHANGE": values[7],
                "TRADE": values[8],
                "VALUE": values[9],
                "VOLUME": values[10],
            }

            result.append(item)

        dataframe=pd.DataFrame(result)
        dataframe.to_csv("share_price.csv")
        print("done")
        await browser.close()

asyncio.run(main())
