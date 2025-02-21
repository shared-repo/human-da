from flask import Blueprint, url_for, session
from flask import request # 요청 관련 정보를 저장하는 객체
from flask import render_template # forward 방식 이동
from flask import redirect # redirect 방식 이동
from werkzeug.security import generate_password_hash # 복원불가능 암호화 도구
from werkzeug.security import check_password_hash # 암호화 데이터 비교

from ..db_utils import auth_util
from ..forms import auth_form

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

# Form을 사용하지 않는 회원가입 처리 구현
# @auth_bp.route("/register/", methods=['GET', 'POST'])
# def register():
#     if request.method.lower() == 'get':
#         return render_template("auth/register.html")
#     else:
#         member_id = request.form.get('memberid', '')
#         passwd = request.form.get('passwd', '')
#         email = request.form.get('email', '')

#         passwd_hash = generate_password_hash(passwd)

#         # print(len(passwd_hash))
#         # print(member_id, passwd, passwd_hash, email)
#         auth_util.insert_member(member_id, passwd_hash, email)

#         # return render_template('auth/login.html') # html로 forward 이동 (서버에서 직접 이동)
#         # return redirect( '/auth/login' ) # view로 redirect 이동 (재요청으로 이동)
#         return redirect( url_for('auth.login') )

# Form을 사용하는 회원가입 처리 구현
@auth_bp.route("/register/", methods=['GET', 'POST'])
def register():
    form = auth_form.RegisterForm()    
    if request.method.lower() == 'post' and form.validate_on_submit():

        print(form.gender.data, request.form.get('gender'))
        print(form.interest.data, request.form.getlist('interest'))
        print(','.join(form.interest.data))
        # return 'test'
    
        passwd_hash = generate_password_hash(form.passwd.data)
        auth_util.insert_member(form.memberid.data, passwd_hash, form.email.data)
        return redirect( url_for('auth.login') )
    else:
        return render_template("auth/register.html", form=form)


# Form을 사용하지 않는 로그인 처리 구현
# @auth_bp.route("/login/", methods=['GET', 'POST'])
# def login():
#     if request.method.lower() == 'get':
#         # return render_template("auth/login2.html")
#         return render_template("auth/login.html")
#     else:
#         member_id = request.form.get('memberid', '')
#         passwd = request.form.get('passwd', '')
#         # print("-------------->", member_id, passwd)

#         # 1. member_id로 데이터베이스에서 데이터 조회
#         member = auth_util.select_member_by_id(member_id)
#         # print("----------------->", member)
#         # 2. 조회된 데이터가 없으면 로그인 실패
#         if not member:
#             return render_template('auth/login.html', 
#                                    error='해당 아이디의 사용자가 없습니다.') # html로 데이터 전달
        
#         # 3. 조회된 데이터가 있으면 패스워드 비교
#         # passwd_hash = generate_password_hash(passwd)
#         # if member[1] == passwd_hash: # generate_password_hash 함수로 만든 데이터는 직접 비교할 수 없음
#         if not check_password_hash(member[1], passwd): # 4. 패스워드가 다르면 로그인 실패
#             return render_template('auth/login.html', 
#                                    error="패스워드가 일치하지 않습니다.")
        
#         else:   # 5. 패스워드가 같으면 로그인 처리
#             # session['loginuser'] = member_id    #  -> 세션에 데이터 저장
#             session['loginuser'] = \
#                 { k: v for k, v in zip(['memberid','passwd', 'email'], member) if k != 'passwd' } 
#             return redirect(url_for("main.index"))

# Form을 사용하는 로그인 처리 구현
@auth_bp.route("/login/", methods=['GET', 'POST'])
def login():
    form = auth_form.LoginForm()
    if request.method.lower() == 'post' and form.validate_on_submit():       

        # 1. member_id로 데이터베이스에서 데이터 조회
        member = auth_util.select_member_by_id(form.memberid.data)
        # 2. 조회된 데이터가 없으면 로그인 실패
        if not member:
            return render_template('auth/login.html', 
                                   form=form,
                                   error='해당 아이디의 사용자가 없습니다.') # html로 데이터 전달
        
        # 3. 조회된 데이터가 있으면 패스워드 비교
        if not check_password_hash(member[1], form.passwd.data): # 4. 패스워드가 다르면 로그인 실패
            return render_template('auth/login.html', 
                                   form=form,
                                   error="패스워드가 일치하지 않습니다.")
        
        else:   # 5. 패스워드가 같으면 로그인 처리
            session['loginuser'] = \
                { k: v for k, v in zip(['memberid','passwd', 'email'], member) if k != 'passwd' } 
            return redirect(url_for("main.index"))
    else:
        # return render_template("auth/login2.html")
        return render_template("auth/login.html", form=form)


@auth_bp.route('/logout', methods=['GET'])
def logout():
    # del session['loginuser']
    # session['loginuser'] = None # session의 한 개 요소만 제거
    session.clear() # 세션의 모든 요소를 제거

    return redirect(url_for('main.index'))

