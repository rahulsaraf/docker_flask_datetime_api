from api import app
from flask import request
from datetime import datetime, timezone
from api import api_classes
import json


@app.route("/time", methods=['GET'])
def get_time():
    req_data = dict()
    if request.data:
        req_data = request.get_json()
    return process_request("time", req_data, current_dt())


@app.route("/date", methods=['GET'])
def get_date():
    req_data = dict()
    if request.data:
        req_data = request.get_json()
    return process_request("date", req_data, current_dt())


@app.route("/datetime", methods=['GET'])
def get_datetime():
    req_data = dict()
    if request.data:
        req_data = request.get_json()
    return process_request("datetime", req_data, current_dt())


def process_request(req_type, req_data, curr_date):
    request_obj = api_classes.construct_request(req_type, req_data)
    response_obj = api_classes.construct_response(req_type, request_obj, curr_date)
    return json.dumps(response_obj.to_dict(request_obj))


def current_dt():
    return datetime.now(timezone.utc)