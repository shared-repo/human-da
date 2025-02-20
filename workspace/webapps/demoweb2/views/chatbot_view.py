from flask import Blueprint, request, jsonify, session, current_app
from openai import OpenAI

chatbot_bp = Blueprint("chatbot", __name__, url_prefix="/chatbot")

# os.environ['OPENAI_API_KEY'] = ""
# cmd 창에서 set OPENAI_API_KEY=api_key
client = OpenAI() # 환경변수에 저장된 api_key를 사용

@chatbot_bp.route("/chat-text/", methods=['POST'])
def handle_chat_text():
    json_data = request.get_json()
    message = json_data.get('message')

    helper = current_app.config['CHROMADB_HELPER']

    selected_recruits = helper.query_similar_documents(message, top_k=5)
    
    recruit_list_str = [f'{idx+1}. {recruit}\n' for idx, recruit 
                        in enumerate(selected_recruits['documents'][0])]

    prompt = f"""             
             아래의 고려사항과 지시사항을 적극적으로 반영해서 질문에 대한 답변을 만들어 주세요.

             ###지시사항###
             1. 채용공고 관련 요청인 경우 채용공고목록을 기반으로 답변을 만듭니다.
             2. 채용공고 관련 요청이 아닌 경우 당신의 기본 지식을 기반으로 답변을 만듭니다.

             ###고려사항###
             1. 사용자는 남성이며 매운음식을 좋아합니다.
             2. 사용자는 민트초코 맛을 매우 좋아합니다.
             3. 사용자는 국물있는 음식도 좋아합니다.
             4. 사용자는 콩국수는 매우 싫어합니다.

             ###채용공고목록###
             {' '.join(recruit_list_str)}

             질문 : {message}
             답변 : """

    chat_history = session.get('chat-history', [])
    if len(chat_history) == 0: # if chat_history:
        chat_history.append({ "role": "system", "content": "당신은 모든 정보를 잘 알고 있는 친절한 안내자입니다. 질문에 대해 가능한 간결하게 답변해야 합니다." })

    chat_history.append({ "role": "user", "content": prompt })

    completion = client.chat.completions.create(
        model="chatgpt-4o-latest",
        messages=chat_history,
        n=1,
        temperature=1
    )

    last_chat = chat_history[-1]
    last_chat['content'] = message
    
    chat_history.append({ "role": "assistant", "content": completion.choices[0].message.content })

    session['chat-history'] = chat_history

    return jsonify({ 'message' : completion.choices[0].message.content })


@chatbot_bp.route("/reload-chat-history/")
def reload_chat_history():
    chat_history = session.get("chat-history", [])

    system_message = """
             당신은 모든 정보를 잘 알고 있는 친절한 안내자입니다. 
             당신은 질문에 대해 가능한 간결하게 답변해야 합니다.
             그리고 아래의 고려사항을 반영해서 답변을 만들어야 합니다.

             [고려사항]
             사용자는 남성이며 매운음식을 좋아합니다.
             사용자는 민트초코 맛을 매우 좋아합니다.
             사용자는 국물있는 음식도 좋아합니다.
             사용자는 콩국수는 매우 싫어합니다."""

    if len(chat_history) == 0: # if chat_history:
        chat_history.append({ "role": "system", "content": "당신은 모든 정보를 잘 알고 있는 친절한 안내자입니다. 질문에 대해 가능한 간결하게 답변해야 합니다." })
        # chat_history.append({ "role": "system", "content": system_message })

    session['chat-history'] = chat_history

    return jsonify( chat_history[1:] if len(chat_history) > 1 else [] )


@chatbot_bp.route("/audio-to-text/", methods=['POST'])
def audio_to_text():
    audio = request.files.get("audio")
    audio.save(audio.filename)

    with open(audio.filename, 'rb') as f:
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=f
        )
    print(transcription.text)
    return transcription.text