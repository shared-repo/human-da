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

def select_board_list(result_type='list'):
    conn = pymysql.connect(host="127.0.0.1", port=3306, db="demoweb",
                           user="humanda", passwd="humanda")
    
    cursor = conn.cursor()

    sql = """select boardno, title, writer, content, readcount, writedate, modifydate, deleted
             from board
             order by boardno desc"""
    cursor.execute(sql)

    rows = cursor.fetchall()    
    
    cursor.close()
    conn.close()

    if result_type == 'list':
        return rows
    else:
        return result_as_dict(rows, ["boardno", "title", "writer", "content", "readcount", "writedate", "modifydate", "deleted"])

def result_as_dict(rows, columns):
    dict_list = []
    for row in rows:
        d = { c:v for c, v in zip(columns, row) }
        dict_list.append(d)
    return dict_list
