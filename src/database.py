import aiosqlite
import asyncio


async def print_db_data():
    connection = await aiosqlite.connect('database.db')
    cursor = await connection.cursor()

    await cursor.execute('SELECT * FROM Stocks')
    stocks = await cursor.fetchall()

    for stock in stocks:
        print(stock)

    await connection.close()


async def get_info_from_db(tkr):
    connection = await aiosqlite.connect('src/database.db')
    cursor = await connection.cursor()
    await cursor.execute('SELECT * FROM Stocks WHERE ticker = (?)', (tkr,))
    stock = await cursor.fetchall()
    await connection.close()
    return stock[0]


# loop = asyncio.get_event_loop()
# G = loop.run_until_complete(print_db_data())
# loop.close()

# tkr = input()
# print(get_info_from_db(tkr))
