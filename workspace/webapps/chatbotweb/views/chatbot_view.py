from flask import Blueprint, request, jsonify, session
from openai import OpenAI
import os

chatbot_bp = Blueprint("chatbot", __name__, url_prefix="/chatbot")

# os.environ['OPENAI_API_KEY'] = ""
# cmd 창에서 set OPENAI_API_KEY=api_key
client = OpenAI() # 환경변수에 저장된 api_key를 사용

# 요청 처리 1 : 폼데이터 읽기 + plain text 반환
# @chatbot_bp.route("/chat-text/", methods=['POST'])
# def handle_chat_text():
#     message = request.form.get('message')
#     print(message)
    
#     return "echo message : " + message

# 요청 처리 2 : JSON 읽기 + JSON 반환  
# @chatbot_bp.route("/chat-text/", methods=['POST'])
# def handle_chat_text():
#     json_data = request.get_json()
#     message = json_data.get('message')

#     print(message)
#     return jsonify({ 'message' : f'echo message : {message}' })

# 요청 처리 3 : openai api service 사용 (simple)
@chatbot_bp.route("/chat-text/", methods=['POST'])
def handle_chat_text():
    json_data = request.get_json()
    message = json_data.get('message')

    completion = client.chat.completions.create(
        model="chatgpt-4o-latest",
        messages=[
            { "role": "system", "content": "당신은 모든 정보를 잘 알고 있는 친절한 안내자입니다. 질문에 대해 가능한 간결하게 답변해야 합니다." },
            { "role": "user", "content": message }
        ],
        n=1,
        temperature=1
    )
    
    return jsonify({ 'message' : completion.choices[0].message.content })


# 요청 처리 4 : openai api service 사용 (대화 history 사용)
@chatbot_bp.route("/chat-text-with-history/", methods=['POST'])
def handle_chat_text_with_history():
    json_data = request.get_json()
    message = json_data.get('message')

    chat_history = session.get('chat-history', [])
    if len(chat_history) == 0: # if chat_history:
        chat_history.append({ "role": "system", "content": "당신은 모든 정보를 잘 알고 있는 친절한 안내자입니다. 질문에 대해 가능한 간결하게 답변해야 합니다." })

    chat_history.append({ "role": "user", "content": message })

    completion = client.chat.completions.create(
        model="chatgpt-4o-latest",
        messages=chat_history,
        n=1,
        temperature=1
    )
    
    chat_history.append({ "role": "assistant", "content": completion.choices[0].message.content })

    session['chat-history'] = chat_history

    return jsonify({ 'message' : completion.choices[0].message.content })


@chatbot_bp.route("/reload-chat-history/")
def reload_chat_history():
    chat_history = session.get("chat-history", [])
    if len(chat_history) == 0: # if chat_history:
        chat_history.append({ "role": "system", "content": "당신은 모든 정보를 잘 알고 있는 친절한 안내자입니다. 질문에 대해 가능한 간결하게 답변해야 합니다." })

    session['chat-history'] = chat_history

    return jsonify( chat_history[1:] if len(chat_history) > 1 else [] )