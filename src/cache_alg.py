from parser import get_scrp_from_trdview, get_stock_tkrs
import aiosqlite
import pandas as pd
import asyncio

async def get_stock_info():
    tickers = await get_stock_tkrs()
    pages, logos = [], []
    result = dict()

    for ticker in tickers:
        info = await get_scrp_from_trdview(ticker)
        pages.append(info["webpage"])
        logos.append(info["logo"])

    result["ticker"] = tickers
    result["page"] = pages
    result["logo"] = logos

    df = pd.DataFrame(result)

    return df


async def cache():
    connection = await aiosqlite.connect('database.db')
    cursor = await connection.cursor()
    data = await get_stock_info()

    await cursor.execute("DROP TABLE IF EXISTS Stocks")
    await connection.commit()

    await cursor.execute('''
    CREATE TABLE IF NOT EXISTS Stocks (
    ticker TEXT,
    page TEXT,
    logo TEXT
    )
    ''')

    for index, row in data.iterrows():
        await cursor.execute("INSERT INTO Stocks (ticker, page, logo) VALUES (?, ?, ?)",
                       (row["ticker"], row["page"], row["logo"]))
        await connection.commit()
    await connection.close()

loop = asyncio.get_event_loop()
G = loop.run_until_complete(cache())

loop.close()