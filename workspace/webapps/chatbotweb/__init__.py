from flask import Flask, render_template
from .views import chatbot_view

def create_app():

    app = Flask(__name__) # webapp 만들기

    app.config['SECRET_KEY'] = 'humanda-secret-key'

    @app.route('/', methods=['GET'])
    def index():
        return render_template("index.html")
    
    app.register_blueprint(chatbot_view.chatbot_bp)
   
    return app