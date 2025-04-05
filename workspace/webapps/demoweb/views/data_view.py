from flask import Blueprint, render_template, request, jsonify, session, current_app

from ..db_utils import data_util

data_bp = Blueprint("data", __name__, url_prefix="/data")

@data_bp.route("/", methods=["GET"])
def index():
    return render_template("data/index.html")
  

@data_bp.route("/get-list/", methods=["GET"])
def get_list():
    quotes = data_util.select_all_quotes()       
    return jsonify(quotes), 200

