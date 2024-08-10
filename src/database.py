import sqlite3


def print_db_data():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Stocks')
    stocks = cursor.fetchall()

    for stock in stocks:
        print(stock)

    connection.close()

def get_info_from_db(tkr):
    connection = sqlite3.connect('src/database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Stocks WHERE ticker = (?)', (tkr,))
    stock = cursor.fetchall()
    connection.close()
    return stock[0]


# print_db_data()

# tkr = input()
# print(get_info_from_db(tkr))