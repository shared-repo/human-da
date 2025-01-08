from flask import Flask, render_template

def create_app():

    app = Flask(__name__) # webapp 만들기

    @app.route("/")
    def index(): 
        return render_template('index.html') # templates/index.html을 처리해서 응답

    return app