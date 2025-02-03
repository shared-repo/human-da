from flask import Flask, render_template, request, redirect, send_from_directory

import os

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
    
    @app.route("/file-upload-test/", methods=['GET'])
    def show_file_upload_page():
        upload_dir = os.path.join(app.root_path, 'upload-files')
        file_names = os.listdir(upload_dir)
        return render_template('file-upload-test.html', fnames=file_names)
    
    @app.route("/file-upload/", methods=['POST'])
    def file_upload():

        if 'attachment' not in request.files: # <input type="file" name="attachment"가 없다면
            return "요청에 파일 선택기가 없습니다."
        if request.files['attachment'].filename == '': # <input type="file" name="attachment"에 파일을 선택하지 않은 경우
            return "파일을 선택하지 않았습니다."
        
        print( request.form.get('formdata') )
        print( request.files['attachment'].filename )

        # print( os.path.join(app.root_path, 'upload-files' ) )
        upload_dir = os.path.join(app.root_path, 'upload-files')
        if (not os.path.exists(upload_dir)):
            os.mkdir(upload_dir)

        file_path = os.path.join(upload_dir, request.files['attachment'].filename)
        request.files['attachment'].save(file_path)

        return redirect("/file-upload-test/")
    

    @app.route("/file-download/")
    def file_download():
        file_name = request.args.get('filename')
        upload_dir = os.path.join(app.root_path, 'upload-files')

        return send_from_directory(upload_dir, file_name, 
                                   as_attachment=True) # mime-type : application/octet-stream

    return app

    