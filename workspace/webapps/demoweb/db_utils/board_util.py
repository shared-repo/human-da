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

    sql = """select boardno, title, writer, readcount, writedate, modifydate, deleted
             from board
             order by boardno desc"""
    cursor.execute(sql)

    rows = cursor.fetchall()    
    
    cursor.close()
    conn.close()

    if result_type == 'list':
        return rows
    else:
        return result_as_dict(rows, ["boardno", "title", "writer", "readcount", "writedate", "modifydate", "deleted"])

def select_board_by_boardno(boardno, result_type='list'):
    conn = pymysql.connect(host="127.0.0.1", port=3306, db="demoweb",
                           user="humanda", passwd="humanda")
    
    cursor = conn.cursor()

    sql = """select boardno, title, writer, content, readcount, writedate, modifydate, deleted
             from board
             where boardno = %s and deleted = FALSE"""
    cursor.execute(sql, [boardno])

    rows = cursor.fetchall()    
    
    cursor.close()
    conn.close()

    if len(rows) == 0:
        return None
    elif result_type == 'list':
        return rows[0]
    else:
        cols = "boardno,title,writer,content,readcount,writedate,modifydate,deleted".split(",")
        results = result_as_dict(rows, cols)
        return results[0]


def result_as_dict(rows, columns):
    dict_list = []
    for row in rows:
        d = { c:v for c, v in zip(columns, row) }
        dict_list.append(d)
    return dict_list

def delete_board(boardno):
    conn = pymysql.connect(host="127.0.0.1", port=3306, db="demoweb",
                           user="humanda", passwd="humanda")
    
    cursor = conn.cursor()

    # sql = """delete board where boardno = %s"""
    sql = """update board set deleted = TRUE where boardno = %s"""
    cursor.execute(sql, [boardno])

    conn.commit()

    cursor.close()
    conn.close()

def update_board(boardno, title, content):
    conn = pymysql.connect(host="127.0.0.1", port=3306, db="demoweb",
                           user="humanda", passwd="humanda")
    
    cursor = conn.cursor()

    sql = """update board set title = %s, content = %s where boardno = %s"""
    cursor.execute(sql, [title, content, boardno])

    conn.commit()

    cursor.close()
    conn.close()
