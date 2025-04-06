from flask import Blueprint, render_template, request, jsonify, session, current_app

import numpy as np
import pandas as pd


from ..db_utils import data_util

data_bp = Blueprint("data", __name__, url_prefix="/data")

@data_bp.route("/", methods=["GET"])
def index():
    return render_template("data/index.html")
  

@data_bp.route("/get-list/", methods=["GET"])
def get_list():
    quotes = data_util.select_all_quotes()       
    return jsonify(quotes), 200


@data_bp.route("/get-price-data/", methods=["GET"])
def get_price_data():
    code = request.args.get("code")
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    quotes = data_util.select_price_data(code, start_date, end_date)
    quotes_ar = np.array(quotes)
    quotes_dict = {}
    for idx, col in enumerate(['code', 'date', 'open', 'high', 'low', 'close', 'volume']):
        if col == 'date':
            quotes_dict[col] = [ str(d)[:10] for d in quotes_ar[:, idx]]
        else:
            quotes_dict[col] = quotes_ar[:, idx].tolist()
    return jsonify(quotes_dict), 200

