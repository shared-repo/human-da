from flask import Flask, render_template
from .views import main_view, auth_view, board_view, serving_view

def create_app():

    app = Flask(__name__) # webapp 만들기

    app.config['SECRET_KEY'] = 'humanda-secret-key'

    # @app.route("/")
    # def index(): 
    #     return render_template('index.html') # templates/index.html을 처리해서 응답

    app.register_blueprint(main_view.main_bp)
    app.register_blueprint(auth_view.auth_bp)
    app.register_blueprint(board_view.board_bp)
    app.register_blueprint(serving_view.serving_bp)


    return app