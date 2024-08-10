from parser import get_scrp_from_trdview, get_stock_tkrs
import sqlite3
import pandas as pd


def get_stock_info():
    tickers = get_stock_tkrs()
    pages, logos = [], []
    result = dict()

    for ticker in tickers:
        info = get_scrp_from_trdview(ticker)
        pages.append(info["webpage"])
        logos.append(info["logo"])

    result["ticker"] = tickers
    result["page"] = pages
    result["logo"] = logos

    df = pd.DataFrame(result)

    return df

def cache():
    connection = sqlite3.connect('src/database.db')
    cursor = connection.cursor()
    data = get_stock_info()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Stocks (
    ticker TEXT,
    page TEXT,
    logo TEXT
    )
    ''')

    for index, row in data.iterrows():
        cursor.execute("INSERT INTO Stocks (ticker, page, logo) VALUES (?, ?, ?)",
                       (row["ticker"], row["page"], row["logo"]))
        connection.commit()
    connection.close()

cache()