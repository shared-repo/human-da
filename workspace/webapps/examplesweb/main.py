from flask import Flask

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

