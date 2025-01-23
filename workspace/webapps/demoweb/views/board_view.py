from flask import Blueprint, render_template, redirect
from flask import request, url_for, session

from ..db_utils import board_util
from ..forms import board_form

board_bp = Blueprint("board", __name__, url_prefix="/board")

# paging 없는 목록 처리
# @board_bp.route("/list/")
# def list():
#     # 데이터 조회 ( db_util 사용 )
#     boards = board_util.select_board_list(result_type='dict')
#     return render_template('board/list.html', boards=boards)

# paging 있는 목록 처리
@board_bp.route("/list/")
def list():
    page_no = request.args.get('page_no', 1) # 요청 데이터는 모두 문자열
    pager = {
        "page_no": int(page_no),   # 현재 페이지 번호
        "page_size": 3,  # 한 페이지에 보여질 글 갯수
        "pager_size": 3, # 한 번에 표시될 페이지 번호 갯수
    }
    data_cnt = board_util.select_board_count()
    pager['page_cnt'] = (data_cnt // pager['page_size']) + \
                        (1 if (data_cnt % pager['page_size']) > 0 else 0)
    pager['page_start'] = ( (pager['page_no'] - 1) // pager['pager_size'] ) * pager['pager_size'] + 1
    pager['page_end'] = pager['page_start'] + pager['pager_size'] 

    start = (pager["page_no"] - 1) * pager["page_size"]
    boards = board_util.select_board_list_with_paging(start, 
                                                      pager["page_size"], 
                                                      result_type='dict')
    return render_template('board/list.html', boards=boards, pager=pager)

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
    
    # boardno에 해당하는 게시글 조회 (db_utils 사용)
    board = board_util.select_board_by_boardno(boardno, result_type='dict')
    if not board:
        return redirect(url_for('board.list'))
    else:
        return render_template('board/detail.html', board=board)

@board_bp.route('/delete/', methods=['GET'])
def delete():
    boardno = request.args.get("boardno")
    if boardno:
        # print('----------------------->', boardno)
        # 데이터베이스에서 boardno로 데이터 삭제 ( db_util 모듈 사용 )
        board_util.delete_board(boardno)

    # 목록으로 이동
    return redirect(url_for('board.list'))

@board_bp.route('/update/', methods=['GET', 'POST'])
def update():
    if request.method.lower() == 'get':
        boardno = request.args.get('boardno')
        if not boardno:
            return redirect(url_for('board.list'))
        
        # boardno에 해당하는 게시글 조회 (db_utils 사용)
        board = board_util.select_board_by_boardno(boardno, result_type='dict')
        if not board:
            return redirect(url_for('board.list'))
        else:
            return render_template('board/update.html', board=board)
    else: # post 요청 처리 영역
        # 요청 데이터 읽기
        boardno = request.form.get('boardno')
        title = request.form.get('title')
        content = request.form.get('content')
        # 데이터베이스의 데이터 수정 (board_util 모듈 사용)
        board_util.update_board(boardno, title, content)

        return redirect(url_for('board.detail', boardno=boardno))
    

    
    
    