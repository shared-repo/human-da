from flask import Blueprint, render_template

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/register/")
def register():
    return render_template("auth/register.html")

@auth_bp.route("/login/")
def login():
    # return render_template("auth/login2.html")
    return render_template("auth/login.html")
