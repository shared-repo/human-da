import pymysql


def insert_board(title, writer, content):
    conn = pymysql.connect(host="127.0.0.1", port=3306, db="demoweb",
                           user="humanda", passwd="humanda")
    
    cursor = conn.cursor()

    sql = """insert into board (title, writer, content)
             values(%s, %s, %s)"""
    cursor.execute(sql, [title, writer, content])

    conn.commit()

    cursor.close()
    conn.close()
