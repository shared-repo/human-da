import pymysql


def insert_member(member_id, passwd, email):
    conn = pymysql.connect(host="db", port=3306, db="demoweb",
                           user="humanda", passwd="humanda")
    
    cursor = conn.cursor()

    sql = """insert into member (memberid, passwd, email)
             values(%s, %s, %s)"""
    cursor.execute(sql, [member_id, passwd, email])

    conn.commit()

    cursor.close()
    conn.close()


def select_member_by_id(member_id):
    conn = pymysql.connect(host="db", port=3306, db="demoweb",
                           user="humanda", passwd="humanda")
    
    cursor = conn.cursor()

    sql = """select memberid, passwd, email
             from member
             where memberid = %s"""
    cursor.execute(sql, [member_id])

    row = cursor.fetchone()

    cursor.close()
    conn.close()

    return row

