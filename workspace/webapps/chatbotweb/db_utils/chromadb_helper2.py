import openai
import chromadb

class ChromadbHelper:

    def __init__(self, db_path, collection_name, init_type='get'):
        self.chromadb_client = chromadb.PersistentClient(path=db_path)
        self.collection_name = collection_name
        if init_type == 'get':
            self.recruit_collection = self.chromadb_client.get_collection(name=collection_name)
        elif init_type == 'create':
            self.recruit_collection = self.chromadb_client.create_collection(name=collection_name)
        elif init_type == 'get_or_create':
            self.recruit_collection = self.chromadb_client.get_or_create_collection(name=collection_name)
        else:
            raise Exception('init_type is not available')

    def generate_embedding(self, text):
        response = openai.embeddings.create(
            input=text,
            model="text-embedding-ada-002"
        )

        # return response['data'][0]['embedding']
        return response.data[0].embedding

    def store_document(self, text):
        embedding = self.generate_embedding(text)

        self.recruit_collection.add(
            documents=[text],
            embeddings=[embedding],
            ids=[text[:50]]
        )

    def query_similar_documents(self, query, top_k=5):
        query_embedding = self.generate_embedding(query)

        results = self.recruit_collection.query( # 유사도를 기반으로 관련성이 높은 데이터 조회 (consine similarity 기본)
            query_embeddings=[query_embedding],
            n_results=top_k
        )
        
        return results

    def delete_collection(self):
        self.chromadb_client.delete_collection(self.collection_name)  


# 아래 if __name__ == "__main__": 은
# import chromdadb_helper 하면 실행되지 않고
# python chromadb_helper.py로 실행하면 실행되는 코드 영역
if __name__ == "__main__": 

    helper = ChromadbHelper('chroma-vectordb', 'recruit_documents')
    
    # documents = [
    #     "오늘 눈이 많이 내립니다. 안전하게 이동해야 합니다.",
    #     "햄버거는 간단하게 점심식사하기에 좋은 음식입니다.",
    #     "인공지는 분야는 전도 유망한 IT 기술 영역입니다.",
    #     "캠핑장은 역시 강원도에 있는 캠핑장이 좋습니다.",
    #     "서브웨이 샌드위치는 주문하기 어려운 음식입니다."
    # ]

    # for doc in documents:
    #     helper.store_document(doc)

    # query = "인공지능이 궁금해요"
    # selected_docs = helper.query_similar_documents(query, top_k=3)
    # for doc, dist in zip(selected_docs['documents'][0], selected_docs['distances'][0]):
    #     print(f'{doc[:20]} : {dist}')

    # helper.delete_collection()

    result = helper.query_similar_documents("파이썬 웹개발자 채용 공고를 알려주세요", top_k=3)
    print("============================================")
    print(result['documents'][0][:2])
