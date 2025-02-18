import openai
import chromadb

chromadb_client = chromadb.PersistentClient(path="chatbotweb/db_utils/chroma-vectordb")
collection_name = "recruit_documents"

recruit_collection = chromadb_client.get_or_create_collection(name=collection_name)

def generate_embedding(text):
    response = openai.embeddings.create(
        input=text,
        model="text-embedding-ada-002"
    )

    # return response['data'][0]['embedding']
    return response.data[0].embedding

def store_document(text):
    embedding = generate_embedding(text)

    recruit_collection.add(
        documents=[text],
        embeddings=[embedding],
        ids=[text[:50]]
    )

def query_similar_documents(query, top_k=5):
    query_embedding = generate_embedding(query)

    results = recruit_collection.query( # 유사도를 기반으로 관련성이 높은 데이터 조회 (consine similarity 기본)
        query_embeddings=[query_embedding],
        n_results=top_k
    )
    
    return results

def delete_collection():
    chromadb_client.delete_collection(collection_name)  


# 아래 if __name__ == "__main__": 은
# import chromdadb_helper 하면 실행되지 않고
# python chromadb_helper.py로 실행하면 실행되는 코드 영역
if __name__ == "__main__": 

    # documents = [
    #     "오늘 눈이 많이 내립니다. 안전하게 이동해야 합니다.",
    #     "햄버거는 간단하게 점심식사하기에 좋은 음식입니다.",
    #     "인공지는 분야는 전도 유망한 IT 기술 영역입니다.",
    #     "캠핑장은 역시 강원도에 있는 캠핑장이 좋습니다.",
    #     "서브웨이 샌드위치는 주문하기 어려운 음식입니다."
    # ]

    # for doc in documents:
    #     store_document(doc)

    # query = "인공지능이 궁금해요"
    # selected_docs = query_similar_documents(query, top_k=3)
    # for doc, dist in zip(selected_docs['documents'][0], selected_docs['distances'][0]):
    #     print(f'{doc[:20]} : {dist}')

    # delete_collection()

    result = query_similar_documents("파이썬 웹개발자 채용 공고를 알려주세요", top_k=3)
    print(result['documents'][0])
