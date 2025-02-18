import pickle
import pymysql

conn = pymysql.connect(
    # host="localhost",
    host="127.0.0.1",
    port=3306,
    user="humanda",
    password="humanda",
    database='demoweb'
)

def remove_all_recruit():
    try:
        with conn.cursor() as cursor:
            sql = "DELETE FROM tbl_recruit"
            cursor.execute(sql)
        
    except Exception as e:
        print(e)
    finally:
        pass

def insert_all_recruit(recruit_list):
    # print(len(recruit_list), len(recruit_list[0]))
    try:
        with conn.cursor() as cursor:
            sql = """   INSERT INTO tbl_recruit (
                                                    company_name, title, etc, detail_info, 
                                                    experience, education, skill, core_competencies, preference, 
                                                    basic_preference, employment_type, salary, region 
                                                )
                        VALUES  ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )"""
            cursor.executemany(sql, recruit_list)
            
        conn.commit()

    except Exception as e:
        conn.rollback()
        print(e)
    finally:
        pass

def load_all_recruits():
    
    try:
        with conn.cursor() as cursor:
            sql = """   SELECT  company_name, title, etc, detail_info, 
                                experience, education, skill, core_competencies, preference, 
                                basic_preference, employment_type, salary, region 
                        FROM tbl_recruit"""
            cursor.execute(sql)

            all_recruits = cursor.fetchall()

    except Exception as e:
        print(e)
    finally:
        pass    

    return all_recruits


if __name__ == "__main__":

    with open('data-files/jobkorea-webdeveloper-detail-20240707.pickle', 'rb') as f:
        recruit_info = pickle.load(f)

    # print(type(recruit_info))
    # print(recruit_info.keys())
    # print(recruit_info['result'], recruit_info['cause'])
    # print(type(recruit_info['data']))
    # print(recruit_info['data'][:3])

    import chromadb_helper

    for idx, row in enumerate(recruit_info['data']):
        doc = ' '.join( [f'[{k}:{v}]' for k, v in row.items()] )
        chromadb_helper.store_document(doc)
        if idx % 20 == 0:
            print(f'{idx + 1}행 처리 완료')

    # selected_docs = chromadb_helper.query_similar_documents('파이썬 웹개발', top_k=5)
    # for doc, dist in zip(selected_docs['documents'][0], selected_docs['distances'][0]):
    #     print(f'{doc[:20]} : {dist}')

    # chromadb_helper.delete_collection()

    



