import pymysql


def select_all_quotes():
    conn = pymysql.connect(
        host='localhost',
        user='developer',
        password='developer',
        db='demoweb'
    )

    try:
        with conn.cursor() as cursor:
            sql = "SELECT code, date, open, high, low, close, volume FROM stock_data limit 10"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    finally:
        conn.close()


def select_price_data(code, start_date, end_date):
    conn = pymysql.connect(
        host='localhost',
        user='developer',
        password='developer',
        db='demoweb'
    )

    try:
        with conn.cursor() as cursor:
            sql = "SELECT code, date, open, high, low, close, volume FROM stock_data where code=%s and date >= %s and date <= %s"
            cursor.execute(sql, (code, start_date, end_date))
            result = cursor.fetchall()
            return result
    finally:
        conn.close()