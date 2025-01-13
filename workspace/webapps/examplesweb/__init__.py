from flask import Flask, render_template, request

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
    
    @app.route('/demo/process-data', methods=['GET'])
    def process_get_data():
        print('process-data : GET handler')
        # request.args : get 방식 전송 데이터 읽기 도구
        a = request.args.get('data_a', "no data for data_a")
        b = request.args.get('data_b', "no data for data_b")
        print(a, b)

        return render_template('demo.html')

    @app.route('/demo/process-data', methods=['POST'])
    def process_post_data():
        print('process-data : POST handler')
        # request.form : post 방식 전송 데이터 읽기 도구
        a = request.form.get('data_a', "no data for data_a")
        b = request.form.get('data_b', "no data for data_b")
        print(a, b)

        return render_template('demo.html')

    return app

    