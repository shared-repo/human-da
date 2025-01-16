from flask import Blueprint, render_template, redirect, request, url_for
from ..db_utils import board_util

board_bp = Blueprint("board", __name__, url_prefix="/board")

@board_bp.route("/list/")
def list():
    return render_template('board/list.html')

@board_bp.route("/write/", methods=['POST', 'GET'])
def write():
    if request.method.lower() == 'post':
        title = request.form.get('title', '')
        writer = request.form.get('writer', '')
        content = request.form.get('content', '')
        # print("================>", title, writer, content)
        board_util.insert_board(title, writer, content)
        return redirect(url_for('board.list'))
    else:
        return render_template('board/write.html')