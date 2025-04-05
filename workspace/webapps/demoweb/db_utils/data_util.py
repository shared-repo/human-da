import pymysql


def select_all_quotes():
    conn = pymysql.connect(
        host='localhost',
        user='humanda5',
        password='humanda5',
        db='humanda5_db'
    )

    try:
        with conn.cursor() as cursor:
            sql = "SELECT code, date, open, high, low, close, volume FROM stock_data limit 10"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    finally:
        conn.close()