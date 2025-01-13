import pymysql


def insert_member(member_id, passwd, email):
    conn = pymysql.connect(host="127.0.0.1", port=3306, db="demoweb",
                           user="humanda", passwd="humanda")
    
    cursor = conn.cursor()

    sql = """insert into member (memberid, passwd, email)
             values(%s, %s, %s)"""
    cursor.execute(sql, [member_id, passwd, email])

    conn.commit()

    cursor.close()
    conn.close()