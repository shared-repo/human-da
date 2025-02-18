from flask import Flask, render_template
from .views import chatbot_view
from .db_utils.chromadb_helper2 import ChromadbHelper

import os

def create_app():

    app = Flask(__name__) # webapp 만들기

    app.config['SECRET_KEY'] = 'humanda-secret-key'

    chroma_db_path = os.path.join(app.root_path, "db_utils", 'chroma-vectordb')
    helper = ChromadbHelper(chroma_db_path, "recruit_documents")
    app.config['CHROMADB_HELPER'] = helper # 웹애플리케이션의 모든 곳에서 공유 가능

    @app.route('/', methods=['GET'])
    def index():
        return render_template("index.html")
    
    app.register_blueprint(chatbot_view.chatbot_bp)
   
    return app