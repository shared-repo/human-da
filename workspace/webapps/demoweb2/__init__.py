from flask import Flask, render_template
from .views import main_view, auth_view, board_view, serving_view, chatbot_view
import os
from .db_utils.chromadb_helper import ChromadbHelper

def create_app():

    app = Flask(__name__) # webapp 만들기

    app.config['SECRET_KEY'] = 'humanda-secret-key'

    chroma_db_path = os.path.join(app.root_path, "db_utils", 'chroma-vectordb')
    helper = ChromadbHelper(chroma_db_path, "recruit_documents")
    app.config['CHROMADB_HELPER'] = helper # 웹애플리케이션의 모든 곳에서 공유 가능

    # @app.route("/")
    # def index(): 
    #     return render_template('index.html') # templates/index.html을 처리해서 응답

    app.register_blueprint(main_view.main_bp)
    app.register_blueprint(auth_view.auth_bp)
    app.register_blueprint(board_view.board_bp)
    app.register_blueprint(serving_view.serving_bp)
    app.register_blueprint(chatbot_view.chatbot_bp)

    return app