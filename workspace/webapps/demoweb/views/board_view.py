from flask import Blueprint, render_template, redirect
from flask import request, url_for, session

from ..db_utils import board_util
from ..forms import board_form

board_bp = Blueprint("board", __name__, url_prefix="/board")

@board_bp.route("/list/")
def list():
    # 데이터 조회 ( db_util 사용 )
    boards = board_util.select_board_list(result_type='dict')
    return render_template('board/list.html', boards=boards)

# Form을 사용하지 않은 write 처리
# @board_bp.route("/write/", methods=['POST', 'GET'])
# def write():
#     if not session.get('loginuser'):    # 로그인하지 않은 사용자는
#         return redirect(url_for('auth.login')) # 로그인 화면으로 보내기
    
#     if request.method.lower() == 'post':
#         title = request.form.get('title', '')
#         writer = request.form.get('writer', '')
#         content = request.form.get('content', '')
#         # print("================>", title, writer, content)
#         board_util.insert_board(title, writer, content)
#         return redirect(url_for('board.list'))
#     else:
#         return render_template('board/write.html')

# Form을 사용하는 write 처리
@board_bp.route("/write/", methods=['POST', 'GET'])
def write():
    if not session.get('loginuser'):    # 로그인하지 않은 사용자는
        return redirect(url_for('auth.login')) # 로그인 화면으로 보내기
    
    form = board_form.BoardForm()

    if request.method.lower() == 'post' and form.validate_on_submit():        
        board_util.insert_board(form.title.data, form.writer.data, form.content.data)
        return redirect(url_for('board.list'))
    else:
        return render_template('board/write.html', form=form)
    
@board_bp.route("/detail/", methods=['GET'])
def detail():
    boardno = request.args.get('boardno')
    if not boardno:
        return redirect(url_for('board.list'))
    
    return render_template('board/detail.html')