import openai

import sys
import io
import base64
from PIL import Image

OPENAI_API_KEY = ""

client = openai.OpenAI(api_key=OPENAI_API_KEY) # openai api service에 연결된 객체

def make_decription_from_image(image_data):
    """이미지에 대한 설명을 만드는 함수"""
    response = client.chat.completions.create(
        model='gpt-4-turbo',
        messages=[
            {
                "role": "user", 
                "content" : [
                    { "type": "text", "text": "이미지에 대해 설명해 주세요" },
                    { 
                        'type': "image_url",
                        'image_url': {
                            'url': image_data
                        }
                    }
                ]
            }
        ],
        max_tokens=1000
    )

    return response.choices[0].message.content

def make_speech_from_description(description, audio_file_name):
    with client.audio.speech.with_streaming_response.create(
        model="tts-1",
        voice="onyx",
        input=description
    ) as response:
        response.stream_to_file(f'data-files/{audio_file_name}')

if __name__ == "__main__":

    # print( sys.argv ) # python xxx.py a b c -> xxx.py, a, b, c
    if not len(sys.argv) == 3:
        print("invalid execution command", end=" ")
        print("--> python program.py image_file_name audio_file_name")
    else:
        image_file_name = sys.argv[1]
        audio_file_name = sys.argv[2]
        # print(image_file_name, audio_file_name)

        # code for file upload
        
        # image = Image.open(image_file_name)
        # buffer = io.BytesIO()
        # image.save(buffer, format="PNG") # 파일을 읽어서 메모리에 저장
        # # 메모리에 저장된 파일 데이터를 base64 방식으로 기록한 binary data 생성 
        # base64_image = base64.b64encode(buffer.getvalue()) 

        with open(image_file_name, "rb") as image_file:
            base64_image = base64.b64encode(image_file.read())
        # binary data -> text data
        base64_string = base64_image.decode("utf-8")

        image_data = f"data:image/*;base64,{base64_string}"

        description = make_decription_from_image(image_data)
        make_speech_from_description(description, audio_file_name)

        print("end of program")
