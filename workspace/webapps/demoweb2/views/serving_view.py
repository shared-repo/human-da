from flask import Blueprint, render_template
from flask import request, jsonify


serving_bp = Blueprint("serving", __name__, url_prefix="/serving")

@serving_bp.route("/index/")
def index():
    return render_template("serving/index.html")

@serving_bp.route("/predict/", methods=['POST'])
def predict():
    # import datetime
    # return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    from PIL import Image
    from tensorflow import keras as tf_keras
    import numpy as np
    from pathlib import Path
    import os

    # 요청 데이터 읽기 ( 이미지 파일 데이터 읽기 )
    files = request.files # 파일 데이터 읽기 ( cf. request.args, request.form )
    if 'img_input' not in files: # img_input 입력 요소가 없는 경우
        return jsonify({
            "result": "fail",
            "message": "No file part"
        }), 400
    
    file = files['img_input']
    if len(file.filename) == 0:      # img_input에 파일이 선택되지 않은 경우
        return jsonify({
            "result": "fail",
            "message": "File not selected"
        }), 400
    
    image_input = Image.open(file) # 파일을 이미지 형식으로 변경
    image_input = image_input.resize((28, 28)) # 모델의 입력 크기에 맞게 이미지 크기 변경
    image_array = tf_keras.utils.img_to_array(image_input)
    image_array /= 255 # 모델의 입력 형식에 맞게 데이터 변경 : 0 ~ 255 -> 0 ~ 1 
    image_array = np.expand_dims(image_array, 0) # 단일 입력을 배치 입력으로 변환

    rpath = serving_bp.root_path # Blueprint가 존재하는 경로
    root_path = Path(rpath).parent # rpath의 부모 경로
    sub_path = 'serving_models/mnist-cnn-model.keras'
    mnist_model = tf_keras.models.load_model(os.path.join(root_path, sub_path))

    predictions = mnist_model.predict(image_array)
    predicted_class = np.argmax(predictions, axis=1)
    confidence = np.max(predictions)

    # return f"[PREDICTED CLASS : {predicted_class}][CONFIDENCE : {confidence}]"
    return jsonify({
        "result": "success",
        "message": "",
        "predicted_class": str(predicted_class),
        "confidence": str(confidence)
    })