from flask import Flask, render_template

def create_app():

    app = Flask(__name__) # webapp 만들기

    @app.route("/")
    def index():
        return "examples-web main"

    @app.route("/hello")
    def hello():
        return "hello, flask web application !!!!!"

    @app.route("/html")
    def html():
        return """
        <html>
            <head><title>hello flask</title></head>
            <body>
                <h2>Hello, Flask Web Application !!!</h2>
            </body>
        </html>"""
    
    @app.route('/demo')
    def show_demo_view():
        return render_template('demo.html')

    return app

    