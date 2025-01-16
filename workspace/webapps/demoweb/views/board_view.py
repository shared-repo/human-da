from flask import Blueprint, render_template, redirect

board_bp = Blueprint("board", __name__, url_prefix="/board")

@board_bp.route("/list/")
def list():
    return render_template('board/list.html')

@board_bp.route("/write/")
def write():
    return render_template('board/write.html')