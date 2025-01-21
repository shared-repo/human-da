from flask import Blueprint, render_template


serving_bp = Blueprint("serving", __name__, url_prefix="/serving")

@serving_bp.route("/index/")
def index():
    return render_template("serving/index.html")