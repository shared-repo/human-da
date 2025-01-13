from flask import Blueprint
from flask import request # 요청 관련 정보를 저장하는 객체
from flask import render_template # forward 방식 이동
from flask import redirect # redirect 방식 이동

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/register/", methods=['GET', 'POST'])
def register():
    if request.method.lower() == 'get':
        return render_template("auth/register.html")
    else:
        member_id = request.form.get('memberid', '')
        passwd = request.form.get('passwd', '')
        email = request.form.get('email', '')

        print(member_id, passwd, email)

        # return render_template('auth/login.html') # html로 forward 이동 (서버에서 직접 이동)
        return redirect( '/auth/login' ) # view로 redirect 이동 (재요청으로 이동)
        

@auth_bp.route("/login/")
def login():
    # return render_template("auth/login2.html")
    return render_template("auth/login.html")
