from flask import Blueprint, render_template

chatbot_bp = Blueprint("chatbot", __name__, url_prefix="/chatbot")

@chatbot_bp.route("/chat-text/")
def handle_chat_text():
    pass